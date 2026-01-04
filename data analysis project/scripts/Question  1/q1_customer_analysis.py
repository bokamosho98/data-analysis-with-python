import pandas as pd
import numpy as np

# 1a. Load dataset and explore
df = pd.read_csv("../data/customers.csv")

print("First 5 rows:")
print(df.head())

print("\nInfo:")
print(df.info())

print("\nDescribe:")
print(df.describe())

# 1b. Mean and standard deviation of age
mean_age = np.mean(df["age"])
std_age = np.std(df["age"])

print("\nMean age:", mean_age)
print("Standard deviation of age:", std_age)

# Boolean array for customers under 25
under_25_bool = df["age"] < 25
print("\nBoolean array (age < 25):")
print(under_25_bool)

# 1c. Filter customers under 25
young_customers = df[under_25_bool]
print("\nCustomers under 25:")
print(young_customers)

# 1d. Create age_group column
def age_group(age):
    if age < 25:
        return "Youth"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

df["age_group"] = df["age"].apply(age_group)

print("\nAge groups added:")
print(df.head())
