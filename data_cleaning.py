"""
Pandas Data Cleaning and Data Manipulation

This program demonstrates:
1. Handling missing values
2. Replacing values
3. Detecting and removing duplicates
4. Creating new columns
5. Handling invalid values
6. Concatenating and merging DataFrames
"""

import pandas as pd
import numpy as np

# Creating a Sample DataFrame

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Alice"],
    "Age": [25, 30, 35, np.nan, 29, 25],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 70000, 62000, np.nan, 50000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Handling Missing Values

print("\nMissing Values:")
print(df.isnull().sum())

df_dropna = df.dropna()
df_fill_zero = df.fillna(0)

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Age"] = df["Age"].ffill()

# Replacing Values

df["Age"] = df["Age"].replace(30, 20)

print("\nAfter Replacing Values:")
print(df)

# Finding Duplicate Records

duplicates_keep_last = df[df.duplicated(keep="last")]
print("\nDuplicates (Keeping Last):")
print(duplicates_keep_last)

duplicates_keep_first = df[df.duplicated(keep="first")]
print("\nDuplicates (Keeping First):")
print(duplicates_keep_first)

# Removing Duplicates

df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)

# Broadcasting Example

df["Promoted Salary"] = df["Salary"] * 100

print("\nAfter Creating Promoted Salary:")
print(df)

# Handling Invalid Values

df["Promoted Salary"] = df["Promoted Salary"].apply(
    lambda x: x / 10 if x > 5000000 else x
)

print("\nAfter Correcting Invalid Values:")
print(df)

# String Splitting Example

# name = "alice_fernandes"
# df[["First_Name", "Last_Name"]] = df["Name"].str.split("_", expand=True)

# Creating Another DataFrame

department_info = {
    "Dept": ["HR", "IT", "Finance"],
    "Location": ["New York", "San Francisco", "Chicago"],
    "Manager": ["Laura", "Steve", "Nina"]
}

df2 = pd.DataFrame(department_info)

# Concatenation

concatenated_df = pd.concat([df, df2])

print("\nConcatenated DataFrame:")
print(concatenated_df)

# Merging DataFrames

merged_df = pd.merge(
    df,
    df2,
    left_on="Department",
    right_on="Dept"
)

print("\nMerged DataFrame:")
print(merged_df)
