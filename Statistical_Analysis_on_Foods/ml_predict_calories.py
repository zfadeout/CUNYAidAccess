import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import scipy.stats as st

# Load and clean the data
cleaned_data = pd.read_csv("cleaned_nutrition_data.csv").dropna()

# Define available features and target variable
all_features = ['total_fat', 'vitamin_a', 'vitamin_b12', 'vitamin_b6', 
                'vitamin_c', 'vitamin_d', 'vitamin_e', 'protein', 
                'carbohydrate', 'fiber', 'sugars']
target = 'calories'

# Function to calculate adjusted R²
def adjusted_r2(r2, n, k):
    """Calculate adjusted R² given R², the number of samples (n), and the number of features (k)."""
    return 1 - (1 - r2) * (n - 1) / (n - k - 1)

# Initialize variables to store the selected features and the current best adjusted R²
selected_features = []
current_r2_adj = 0

# Feature selection loop
while True:
    improvements = []  # Store the R² improvements for each feature not yet selected
    
    # Evaluate adding each feature that has not yet been selected
    for feature in all_features:
        if feature not in selected_features:
            # Create a temporary feature set with the current feature included
            temp_features = selected_features + [feature]
            X_temp = cleaned_data[temp_features]
            y = cleaned_data[target]
            
            # Normalize the feature data
            scaler = StandardScaler()
            X_temp_normalized = scaler.fit_transform(X_temp)
            
            # Fit the model with the normalized features
            model = LinearRegression().fit(X_temp_normalized, y)
            y_pred = model.predict(X_temp_normalized)
            r2 = r2_score(y, y_pred)
            r2_adj = adjusted_r2(r2, len(y), len(temp_features))
            
            # Store the feature and its adjusted R² value
            improvements.append((feature, r2_adj))
    
    # Find the feature that provides the highest adjusted R²
    best_feature, best_r2_adj = max(improvements, key=lambda x: x[1])
    
    # Add the best feature if it improves the adjusted R²
    if best_r2_adj > current_r2_adj:
        selected_features.append(best_feature)
        current_r2_adj = best_r2_adj
        print(f"Added {best_feature}, Adjusted R²: {current_r2_adj:.4f}")
    else:
        # Stop if no further improvement in adjusted R²
        print("No further improvement in Adjusted R².")
        break

# Final model with the selected features
X_final = cleaned_data[selected_features]

# Normalize the selected features
scaler = StandardScaler()
X_final_normalized = scaler.fit_transform(X_final)

# Store means and standard deviations for the normalization equation
means = scaler.mean_
std_devs = scaler.scale_

y_final = cleaned_data[target]
final_model = LinearRegression().fit(X_final_normalized, y_final)
final_r2 = r2_score(y_final, final_model.predict(X_final_normalized))
final_r2_adj = adjusted_r2(final_r2, len(y_final), len(selected_features))

# Calculate the standard error of the predictions
se_final = np.sqrt(np.sum((y_final - final_model.predict(X_final_normalized)) ** 2) / (len(y_final) - len(selected_features) - 1))
t_value = st.t.ppf(0.975, df=len(y_final) - len(selected_features) - 1)

# Output final model summary
print("\nFinal Model Summary:")
print(f"Selected Features: {selected_features}")
print(f"Final Adjusted R²: {final_r2_adj:.4f}")

# Generate regression equation text with normalization and confidence interval included
equation_text = f'y = {final_model.intercept_:.2f}'

for i, (coef, feature) in enumerate(zip(final_model.coef_, selected_features)):
    equation_text += f' + {coef:.2f} * (({feature.replace("_", " ").capitalize()} - {means[i]:.2f}) / {std_devs[i]:.2f})'

equation_text += f'\nAdjusted R² = {final_r2_adj:.4f}'
equation_text += f'\nSE = {se_final:.2f}, 95% CI = y ± {t_value:.2f} * SE'

# Plot and save the regression equation
plt.figure(figsize=(10, 2))
plt.text(0.5, 0.5, equation_text, fontsize=14, ha='center', va='center', wrap=True)
plt.axis('off')
plt.tight_layout()
plt.savefig('multivariable_regression_equation_with_normalization_and_ci.png')
plt.show()

# ----- Second Model with Fixed Features: Total Fat, Carbohydrates, Protein -----

fixed_features = ['total_fat', 'carbohydrate', 'protein']

# Fit the model
X_fixed = cleaned_data[fixed_features]

# Normalize the fixed features
scaler_fixed = StandardScaler()
X_fixed_normalized = scaler_fixed.fit_transform(X_fixed)

# Store means and standard deviations for the normalization equation
means_fixed = scaler_fixed.mean_
std_devs_fixed = scaler_fixed.scale_

y_fixed = cleaned_data[target]
fixed_model = LinearRegression().fit(X_fixed_normalized, y_fixed)
fixed_r2 = r2_score(y_fixed, fixed_model.predict(X_fixed_normalized))
fixed_r2_adj = adjusted_r2(fixed_r2, len(y_fixed), len(fixed_features))

# Calculate the standard error of the predictions
se_fixed = np.sqrt(np.sum((y_fixed - fixed_model.predict(X_fixed_normalized)) ** 2) / (len(y_fixed) - len(fixed_features) - 1))

print("\nFixed Model Summary (Total Fat, Carbohydrates, Protein):")
print(f"Fixed Features: {fixed_features}")
print(f"Adjusted R²: {fixed_r2_adj:.4f}")

# Generate regression equation text for the fixed model with normalization and confidence interval included
fixed_equation_text = f'y = {fixed_model.intercept_: .2f}'

for i, (coef, feature) in enumerate(zip(fixed_model.coef_, fixed_features)):
    fixed_equation_text += f' + {coef:.2f} * (({feature.capitalize()} - {means_fixed[i]:.2f}) / {std_devs_fixed[i]:.2f})'

fixed_equation_text += f'\nAdjusted R² = {fixed_r2_adj:.4f}'
fixed_equation_text += f'\nSE = {se_fixed:.2f}, 95% CI = y ± {t_value:.2f} * SE'

# Plot and save the regression equation
plt.figure(figsize=(10, 2))
plt.text(0.5, 0.5, fixed_equation_text, fontsize=14, ha='center', va='center', wrap=True)
plt.axis('off')
plt.tight_layout()
plt.savefig('fixed_features_regression_equation_with_normalization_and_ci.png')
plt.show()

vif_data = pd.DataFrame()
vif_data["Feature"] = selected_features

# Output VIF data
print("\nVariance Inflation Factor (VIF) for selected features:")
print(vif_data)
