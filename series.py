import pandas as pd

# Creating a Pandas Series
numbers = pd.Series([10, 2, 11, 20, 5])

print("Series:\n", numbers)
print("\nData Type:", numbers.dtype)
print("Values:", numbers.values)
print("Indexes:", numbers.index)

# Assigning a name to the Series
numbers.name = "Numbers"
print("\nSeries Name:", numbers.name)

# Indexing Operations

# Accessing a single element
print("\nFirst Element:", numbers[0])

# Slicing the Series
print("\nFirst Three Elements:\n", numbers[0:3])

# iloc -> Position-based indexing
print("\nElements at Positions 2 and 4:\n", numbers.iloc[[2, 4]])

# Changing Index Labels
new_indexes = [1, 2, 3, 4, 5]
numbers.index = new_indexes

print("\nSeries After Changing Indexes:\n", numbers)

# Accessing value using index label
print("\nValue at Index 2:", numbers[2])

# loc -> Label-based indexing
# In loc slicing, both start and end values are included

print("\nValue at Label 3:", numbers.loc[3])

print("\nValues from Label 1 to 3:\n", numbers.loc[1:3])

# Creating a Series from a Dictionary
fruits = {
    "Guava": 74,
    "Kiwi": 90,
    "Mango": 87
}

fruit_series = pd.Series(fruits)

print("\nFruit Series:\n", fruit_series)

# condisional selection
print(fruit_series[fruit_series>80])

# logical operator
s = pd.Series([10, 25, 40, 55, 70])

print("Series:\n", s)

# AND Operator
print("\nAND Operator:")
print((s > 20) & (s < 60))

# OR Operator
print("\nOR Operator:")
print((s < 20) | (s > 50))

# NOT Operator
print("\nNOT Operator:")
print(~(s > 30))