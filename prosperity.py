import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# Set the style for seaborn plots
sns.set(style="whitegrid")

# Load the main dataset
nlsy97_data = pd.read_csv("NLSY97_subset.csv")

# Load the variable names and descriptions
variable_desc = pd.read_csv("NLSY97_Variable_Names_and_Descriptions.csv")

# Display the first few rows of the main dataset
print("Main Dataset:")
print(nlsy97_data.head())

# Display the variable names and descriptions
print("\nVariable Names and Descriptions:")
print(variable_desc)

# Check for duplicate rows in the dataset
duplicate_rows = nlsy97_data.duplicated()

# Count the number of duplicate rows
num_duplicates = duplicate_rows.sum()
print("Number of duplicate rows:", num_duplicates)

# Remove duplicate rows from the dataset
cleaned_data = nlsy97_data.drop_duplicates()

# Check the shape of the cleaned dataset
print("Shape of cleaned dataset:", cleaned_data.shape)


# Compute descriptive statistics for the dataset
descriptive_stats = cleaned_data.describe()

# Print the descriptive statistics
print(descriptive_stats)

# Visualize the distribution of earnings
plt.figure(figsize=(10, 6))
sns.histplot(cleaned_data['EARNINGS'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Earnings')
plt.xlabel('Earnings')
plt.ylabel('Frequency')
plt.show()

# Visualize the relationship between earnings and years of schooling
plt.figure(figsize=(10, 6))
sns.scatterplot(x='S', y='EARNINGS', data=cleaned_data, color='salmon')
plt.title('Earnings vs. Years of Schooling')
plt.xlabel('Years of Schooling')
plt.ylabel('Earnings')
plt.show()

# Visualize the boxplot of earnings by sex
plt.figure(figsize=(10, 6))
sns.boxplot(x='FEMALE', y='EARNINGS', data=cleaned_data, palette='Set2')
plt.title('Boxplot of Earnings by Sex')
plt.xlabel('Sex (0: Male, 1: Female)')
plt.ylabel('Earnings')
plt.show()

# Train_Test

# Define the features (X) and target variable (y)
X = cleaned_data.drop(columns=['EARNINGS'])  # Features
y = cleaned_data['EARNINGS']  # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Print the shapes of the training and testing sets
print("Training set shape:", X_train.shape, y_train.shape)
print("Testing set shape:", X_test.shape, y_test.shape)

# Simple Linear Regression

# Create a linear regression model
model = LinearRegression()

# Fit the model on the training data
model.fit(X_train[['S']], y_train)

# Make predictions on the training data
y_pred_train = model.predict(X_train[['S']])

# Calculate R-squared for the regression on the training data
r_squared_train = r2_score(y_train, y_pred_train)
print("R-squared for the regression on the training data:", r_squared_train)

# Retrieve the coefficient for the 'S' variable
coefficient_S = model.coef_[0]
print("Coefficient for the 'S' variable:", coefficient_S)

"""Interpreting this coefficient, we can say that for each additional year of schooling,
earnings are expected to increase by approximately $1.27, holding all other variables constant.
This implies that education has a positive effect on earnings,
with individuals earning higher incomes with each additional year of schooling on average."""

# Analyse the Estimated Values & Regression Residuals
# Calculate residuals
residuals = y_train - y_pred_train

# Plot predicted values vs. true values
plt.figure(figsize=(10, 6))
plt.scatter(y_pred_train, y_train, alpha=0.5)
plt.plot([min(y_pred_train), max(y_pred_train)], [min(y_pred_train), max(y_pred_train)], color='red', linestyle='--')
plt.title('Predicted Values vs. True Values (Training Data)')
plt.xlabel('Predicted Earnings')
plt.ylabel('True Earnings')
plt.show()

# Plot histogram of residuals
plt.figure(figsize=(10, 6))
sns.histplot(residuals, bins=20, kde=True)
plt.title('Histogram of Residuals')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.show()

# Multivariable Regression

# Initialize Linear Regression model
model_multi = LinearRegression()

# Fit the model on the training data using both 'S' and 'EXP' variables
model_multi.fit(X_train[['S', 'EXP']], y_train)

# Predict earnings on the training data
y_train_pred_multi = model_multi.predict(X_train[['S', 'EXP']])

# Calculate r-squared for
r_squared_train_multi = r2_score(y_train, y_train_pred_multi)
print("R-squared for multivariable regression on the training data:", r_squared_train_multi)

#Get the coefficients of the model
coefficients_multi = model_multi.coef_

#Print the coefficients
print("Coefficients for multivariable regression:")
print("Coefficient for 'S' (years of schooling):", coefficients_multi[0])
print("Coefficient for 'EXP' (years of work experience):", coefficients_multi[1])

#Analyse the Estimated Values & Regression Residuals
#Calculate residuals for multivariable regression
residuals_multi = y_train - y_train_pred_multi

#Plot predicted values vs. true values for multivariable regression
plt.figure(figsize=(10, 6))
plt.scatter(y_train_pred_multi, y_train, alpha=0.5)
plt.plot([min(y_train_pred_multi), max(y_train_pred_multi)], [min(y_train_pred_multi), max(y_train_pred_multi)], color='red', linestyle='--')
plt.title('Predicted Values vs. True Values (Multivariable Regression)')
plt.xlabel('Predicted Earnings')
plt.ylabel('True Earnings')
plt.show()

#Plot histogram of residuals for multivariable regression
plt.figure(figsize=(10, 6))
sns.histplot(residuals_multi, bins=20, kde=True)
plt.title('Histogram of Residuals (Multivariable Regression)')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.show()

# Multivariable Regression
# Calculate r-squared for the regression on the training data
r_squared_train_multi = r2_score(y_train, y_train_pred_multi)
print("R-squared for multivariable regression on the training data:", r_squared_train_multi)


# Get the coefficients of the model
coefficients_multi = model_multi.coef_

# Print the coefficients
print("Coefficients for multivariable regression:")
print("Coefficient for 'S' (years of schooling):", coefficients_multi[0])
print("Coefficient for 'EXP' (years of work experience):", coefficients_multi[1])

# Analyse the Estimated Values & Regression Residuals

# Plot predicted values vs. true values
plt.figure(figsize=(10, 6))
plt.scatter(y_pred_train, y_train, alpha=0.5)
plt.plot([min(y_pred_train), max(y_pred_train)], [min(y_pred_train), max(y_pred_train)], color='red', linestyle='--')
plt.title('Predicted Values vs. True Values (Training Data)')
plt.xlabel('Predicted Earnings')
plt.ylabel('True Earnings')
plt.show()

# Plot histogram of residuals
plt.figure(figsize=(10, 6))
sns.histplot(residuals, bins=20, kde=True)
plt.title('Histogram of Residuals')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.show()


#Make prediction

# Define the feature names
feature_names = ['S', 'EXP']

# Define the features for the individual
years_of_schooling = 16  # Bachelor's degree (12 years + 4 years)
years_of_experience = 5
features = [[years_of_schooling, years_of_experience]]

# Use the trained multivariable regression model to predict earnings
predicted_earnings = model_multi.predict(features)

# Print the predicted earnings
print("Predicted earnings for someone with 16 years of schooling and 5 years of work experience:", predicted_earnings[0])
