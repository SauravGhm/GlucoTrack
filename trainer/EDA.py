import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
shared_path = "/app/shared"

# Create directories if they don't exist
os.makedirs("shared/data", exist_ok=True)
os.makedirs("shared/models", exist_ok=True)

data_file = os.path.join(shared_path, "data", "processed_data.csv")

# Example mock preprocessing (fill this with real logic as needed)
df = pd.read_csv('https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv', header=None)  # replace with real path to raw data
df.columns = [
    'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
    'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'
]
# Check missing values (0s as missing)
zero_cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
for col in zero_cols:
    print(f"{col} has {(df[col] == 0).sum()} zero values")

# Replace zeros with median
for col in zero_cols:
    df[col] = df[col].replace(0, df[col].median())

# Class distribution
sns.countplot(x='Outcome', data=df)
plt.title('Diabetes Class Distribution')
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.show()

# Histograms
df.hist(bins=20, figsize=(12, 10))
plt.suptitle('Feature Distributions', fontsize=16)
plt.show()

df.to_csv(data_file, index=False)
