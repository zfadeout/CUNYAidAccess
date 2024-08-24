import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import scipy.stats as st

# Load and clean the data
cleaned_data = pd.read_csv("cleaned_nutrition_data.csv")

# Define available features for analysis
features = ['total_fat', 'vitamin_a', 'vitamin_b12', 'vitamin_b6', 
            'vitamin_c', 'vitamin_d', 'vitamin_e', 'protein', 
            'carbohydrate', 'fiber', 'sugars']

print("Available features to analyze:")
for i, feature in enumerate(features, start=1):
    print(f"{i}. {feature.replace('_', ' ').capitalize()}")

# Get user input for feature selection
selection = int(input(f"Select a feature to analyze (1-{len(features)}): "))

# Validate user input
if selection < 1 or selection > len(features):
    print("Invalid selection. Please run the script again and choose a valid number.")
else:
    # Get selected feature
    feature = features[selection - 1]

    # Prepare the data for the selected feature
    cleaned_data = cleaned_data[[feature, 'calories']].dropna()
    X = cleaned_data[[feature]]
    y = cleaned_data['calories']

    # Normalize the feature data
    scaler = StandardScaler()
    X_normalized = scaler.fit_transform(X)

    # Extract mean and std from the scaler
    feature_mean = scaler.mean_[0]
    feature_std = scaler.scale_[0]

    # Convert X to a NumPy array for plotting
    X_numpy = X.to_numpy()

    # ----- Linear Regression -----
    linear_model = LinearRegression()
    linear_model.fit(X_normalized, y)
    y_pred_linear = linear_model.predict(X_normalized)

    r2_linear = r2_score(y, y_pred_linear)

    intercept_linear = linear_model.intercept_
    coef_linear = linear_model.coef_[0]

    # Calculate the standard error of the predictions
    se_line = np.sqrt(np.sum((y - y_pred_linear) ** 2) / (len(y) - 2))
    t_value = st.t.ppf(0.975, df=len(y) - 2)
    ci_upper_linear = y_pred_linear + t_value * se_line
    ci_lower_linear = y_pred_linear - t_value * se_line

    print(f"R² score for linear model: {r2_linear:.4f}")

    plt.figure(figsize=(10, 6))
    plt.scatter(X_numpy, y, color="blue", label="Actual Data")
    plt.plot(X_numpy, y_pred_linear, color='red', label='Linear Fit', linewidth=2)
    plt.fill_between(X_numpy.ravel(), ci_lower_linear, ci_upper_linear, color='red', alpha=0.2, label="95% CI")

    # Adjusting the legend location to avoid overlapping with the annotation text
    plt.legend(loc='upper left')

    # Moving the annotation to the bottom right to avoid overlap
    plt.text(
        0.95, 0.05,
        f'Linear Equation: y = {intercept_linear:.2f} + {coef_linear:.2f} * (X - {feature_mean:.2f}) / {feature_std:.2f}\n'
        f'R² = {r2_linear:.4f}\n'
        f'Mean: {feature_mean:.2f}, Std: {feature_std:.2f}\n'
        f'SE: {se_line:.2f}, 95% CI: y ± {t_value:.2f} * SE',
        transform=plt.gca().transAxes,
        fontsize=12,
        verticalalignment='bottom',
        horizontalalignment='right',
        bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor="black")
    )

    plt.xlabel(f'{feature.replace("_", " ").capitalize()}')
    plt.ylabel('Calories')
    plt.title(f'Linear Regression: {feature.replace("_", " ").capitalize()} vs. Calories')
    plt.tight_layout()

    # Ask the user if they want to save the graph
    save_graph = input("Do you want to save the linear regression graph? (yes/no): ").strip().lower()
    if save_graph == 'yes':
        plt.savefig(f'{feature}_linear_regression.png')

    plt.show()

    # ----- Nonlinear Regression (Quadratic) -----
    cleaned_data[f'{feature}_squared'] = cleaned_data[feature] ** 2
    X_poly = cleaned_data[[feature, f'{feature}_squared']]

    # Normalize the polynomial features
    X_poly_normalized = scaler.fit_transform(X_poly)

    poly_model = LinearRegression()
    poly_model.fit(X_poly_normalized, y)
    y_pred_poly = poly_model.predict(X_poly_normalized)

    r2_poly = r2_score(y, y_pred_poly)

    intercept_poly = poly_model.intercept_
    coef_poly = poly_model.coef_

    # Calculate the standard error of the predictions
    se_poly = np.sqrt(np.sum((y - y_pred_poly) ** 2) / (len(y) - 3))
    ci_upper_poly = y_pred_poly + t_value * se_poly
    ci_lower_poly = y_pred_poly - t_value * se_poly

    print(f"R² score for quadratic model: {r2_poly:.4f}")

    sorted_zip = sorted(zip(cleaned_data[feature], y_pred_poly, ci_lower_poly, ci_upper_poly))
    X_sorted, y_pred_poly_sorted, ci_lower_poly_sorted, ci_upper_poly_sorted = zip(*sorted_zip)

    plt.figure(figsize=(10, 6))
    plt.scatter(X_numpy, y, color="blue", label="Actual Data")
    plt.plot(X_sorted, y_pred_poly_sorted, color='green', label='Quadratic Fit', linewidth=2)
    plt.fill_between(X_sorted, ci_lower_poly_sorted, ci_upper_poly_sorted, color='green', alpha=0.2, label="95% CI")

    # Adjusting the legend location to avoid overlapping with the annotation text
    plt.legend(loc='upper left')

    # Moving the annotation to the bottom right to avoid overlap
    plt.text(
        0.95, 0.05,
        f'Quadratic Equation: y = {intercept_poly:.2f} + {coef_poly[0]:.2f} * (X - {feature_mean:.2f}) / {feature_std:.2f} + {coef_poly[1]:.4f} * ((X - {feature_mean:.2f}) / {feature_std:.2f})²\n'
        f'R² = {r2_poly:.4f}\n'
        f'Mean: {feature_mean:.2f}, Std: {feature_std:.2f}\n'
        f'SE: {se_poly:.2f}, 95% CI: y ± {t_value:.2f} * SE',
        transform=plt.gca().transAxes,
        fontsize=12,
        verticalalignment='bottom',
        horizontalalignment='right',
        bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor="black")
    )

    plt.xlabel(f'{feature.replace("_", " ").capitalize()}')
    plt.ylabel('Calories')
    plt.title(f'Quadratic Regression: {feature.replace("_", " ").capitalize()} vs. Calories')
    plt.tight_layout()

    # Ask the user if they want to save the quadratic regression graph
    save_graph = input("Do you want to save the quadratic regression graph? (yes/no): ").strip().lower()
    if save_graph == 'yes':
        plt.savefig(f'{feature}_quadratic_regression.png')

    plt.show()

