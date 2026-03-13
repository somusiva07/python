import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

# print(new_df.to_string())

x = df["Calories"].mean()

df.fillna({"Calories": x}, inplace=True)

# print(df.to_string())

x = df["Calories"].median()

df.fillna({"Calories": x}, inplace=True)

# print(df.to_string())


x = df["Calories"].mode()

df.fillna({"Calories": x}, inplace=True)

print(df.to_string())