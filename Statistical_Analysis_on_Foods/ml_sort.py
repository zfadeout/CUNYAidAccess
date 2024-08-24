import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.mixture import GaussianMixture
import numpy as np
import scipy.stats as st

data = pd.read_csv("nutrition.csv").dropna()

# Remove any measurement units (like 'g', 'mg', etc.) and keep only the numbers
def remove_units(value):
    if isinstance(value, str):
        filtered_value = ''.join(filter(lambda x: x.isdigit() or x == '.', value))
        try:
            return float(filtered_value) if filtered_value.replace('.', '', 1).isdigit() else 0.0
        except ValueError:
            return 0.0
    return value

for column in data.columns:
    if column != 'name':
        data[column] = data[column].apply(remove_units)


X = data[['sugars', 'calories']]

scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)

gmm = GaussianMixture(n_components=2, random_state=0)
data['GMM_Cluster'] = gmm.fit_predict(X_normalized)

cluster_stats = data.groupby('GMM_Cluster').agg({'sugars': ['mean', 'std'], 'calories': ['mean', 'std']})
print("\nCluster Statistics (Mean and Std):")
print(cluster_stats)

high_sugar_cluster = cluster_stats['sugars']['mean'].idxmax()
print(f"\nHigh sugar cluster identified: {high_sugar_cluster}")

filtered_data = data[data['GMM_Cluster'] != high_sugar_cluster].copy()

selected_features = ['total_fat', 'vitamin_a', 'vitamin_b12', 'vitamin_b6', 
                     'vitamin_c', 'vitamin_d', 'vitamin_e', 'protein', 
                     'carbohydrate', 'fiber', 'sugars']

X_filtered = filtered_data[selected_features]
y_filtered = filtered_data['calories']

X_filtered_normalized = scaler.fit_transform(X_filtered)

final_model = LinearRegression().fit(X_filtered_normalized, y_filtered)

filtered_data.loc[:, 'predicted_calories'] = final_model.predict(X_filtered_normalized)

se = np.sqrt(np.sum((y_filtered - filtered_data['predicted_calories']) ** 2) / (len(y_filtered) - len(selected_features) - 1))

# Calculate the 65% confidence interval
t_value_65 = st.t.ppf(0.825, df=len(y_filtered) - len(selected_features) - 1)
filtered_data.loc[:, 'ci_lower'] = filtered_data['predicted_calories'] - t_value_65 * se
filtered_data.loc[:, 'ci_upper'] = filtered_data['predicted_calories'] + t_value_65 * se

# Filter for items with negative calorie difference and outside the 65% confidence interval
filtered_data.loc[:, 'calorie_difference'] = filtered_data['calories'] - filtered_data['predicted_calories']
negative_calorie_difference_data = filtered_data[(filtered_data['calorie_difference'] < 0) & 
                                                 ((filtered_data['calories'] < filtered_data['ci_lower']) | 
                                                  (filtered_data['calories'] > filtered_data['ci_upper']))]
sorted_negative_calorie_data = negative_calorie_difference_data.sort_values(by='calorie_difference')

# Save the filtered items to a text file in the current working directory
with open("filtered_negative_calorie_difference_items.txt", "w") as file:
    for index, row in sorted_negative_calorie_data.iterrows():
        file.write(f"Name: {row['name']}\n")
        file.write(f"Total Fat: {row['total_fat']}g\n")
        file.write(f"Vitamin A: {row['vitamin_a']} IU\n")
        file.write(f"Vitamin B12: {row['vitamin_b12']} µg\n")
        file.write(f"Vitamin B6: {row['vitamin_b6']} mg\n")
        file.write(f"Vitamin C: {row['vitamin_c']} mg\n")
        file.write(f"Vitamin D: {row['vitamin_d']} IU\n")
        file.write(f"Vitamin E: {row['vitamin_e']} mg\n")
        file.write(f"Protein: {row['protein']}g\n")
        file.write(f"Carbohydrate: {row['carbohydrate']}g\n")
        file.write(f"Fiber: {row['fiber']}g\n")
        file.write(f"Sugars: {row['sugars']}g\n")
        file.write(f"Actual Calories: {row['calories']}\n")
        file.write(f"Predicted Calories: {row['predicted_calories']:.2f}\n")
        file.write(f"Calorie Difference (Actual - Predicted): {row['calorie_difference']:.2f}\n")
        file.write(f"95% CI: [{row['ci_lower']:.2f}, {row['ci_upper']:.2f}]\n")
        file.write("\n" + "-"*40 + "\n\n")

print(f"\nNumber of foods left after filtering: {len(sorted_negative_calorie_data)}")

print("Filtered items saved to 'filtered_negative_calorie_difference_items.txt'")
