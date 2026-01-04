import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("../data/customers.csv")

# Re-create age_group (needed again)
df["age_group"] = df["age"].apply(
    lambda x: "Youth" if x < 25 else "Adult" if x < 60 else "Senior"
)

# 2a. Convert subscription_date
df["subscription_date"] = pd.to_datetime(df["subscription_date"])
df["year_joined"] = df["subscription_date"].dt.year
df["month_joined"] = df["subscription_date"].dt.month
df["quarter_joined"] = df["subscription_date"].dt.to_period("Q").astype(str)

# 2b. Groupby age_group
grouped = df.groupby("age_group").agg(
    avg_age=("age", "mean"),
    avg_year_joined=("year_joined", "mean")
)
print(grouped)

# 2c. Bar chart: sign-ups per year
df["year_joined"].value_counts().sort_index().plot(kind="bar")
plt.title("Number of Sign-ups per Year")
plt.xlabel("Year")
plt.ylabel("Number of Customers")
plt.show()

# 2d. Pie chart: age_group distribution
df["age_group"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Customer Distribution by Age Group")
plt.ylabel("")
plt.show()

# 2e. Save cleaned dataset
df.to_csv("../outputs/community_customers_cleaned.csv", index=False)

print("Cleaned dataset saved.")
