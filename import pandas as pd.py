import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder

# Load dataset (Kaggle Titanic dataset)
df = pd.read_csv("titanic.csv")

# Preview data
print(df.head())
print(df.info())

# Check missing values
print("\nMissing values before handling:")
print(df.isnull().sum())

# Fill Age with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill Embarked with mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Drop Cabin (too many missing values)
df.drop(columns=['Cabin'], inplace=True)

print("\nMissing values after handling:")
print(df.isnull().sum())
Step 4: Feature Encoding

# Label encode 'Sex'
le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])   # male=1, female=0

# One-hot encode 'Embarked'
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)


scaler = StandardScaler()

# Scale numerical features
num_cols = ['Age', 'Fare']
df[num_cols] = scaler.fit_transform(df[num_cols])



# Select features to visualize
sns.pairplot(df[['Survived', 'Age', 'Fare', 'Sex']], hue='Survived', diag_kind="kde")
plt.show()
