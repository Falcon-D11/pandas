import pandas as pd
import numpy as np

# Creating a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Alice"],
    "Age": [25, 30, 35, np.nan, 29, 25],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 70000, 62000, np.nan, 50000]
}

df = pd.DataFrame(data)

print(df)

# Displaying starting rows
print(df.head(5))

# Displaying ending rows
print(df.tail(3))

# Using iloc (Position-based indexing)
print(df.iloc[1:3])

# Using loc (Label-based indexing)
print(df.loc[1:2, ["Age", "Department"]])

# Accessing a single column
print(df["Age"])

# Dropping a column
print(df.drop("Age", axis=1))

# Shape of DataFrame
print(df.shape)

# Information about DataFrame
print(df.info())

# Statistical Summary
print(df.describe())

# Updating Salary Column
df["Salary"] = df["Salary"] + 5000

print(df)

# Renaming Columns
df.rename(columns={"Department": "Dept"}, inplace=True)
 # inplace=True if we want change in original dataframe

print(df)

# Unique Values
print(df["Dept"].unique())

# Value Counts
print(df["Dept"].value_counts())