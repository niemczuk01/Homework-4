import pandas as pd

df = pd.read_csv("data/swimmers_times.csv")

print("\n=== FIRST 5 ROWS ===")
print(df.head())

print("\n=== INFO ===")
print(df.info())

print("\n=== DESCRIBE ===")
print(df.describe(include='all'))

print("\n=== ROW 0 (loc) ===")
print(df.loc[0])

print("\n=== ROW 0 (iloc) ===")
print(df.iloc[0])

print("\n=== SLICE 0:3 ===")
print(df.iloc[0:3])

print("\n=== COLUMN: Event ===")
print(df["Event"])

print("\n=== CELL [0, 'Time'] ===")
print(df.loc[0, "Time"])
