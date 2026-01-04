import pandas as pd
import matplotlib.pyplot as plt
import re

# 3a. Load and explore
df = pd.read_csv("../data/health_data.csv")

print(df.info())
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicates:", df.duplicated().sum())

# 3b. Clean blood_pressure using regex
df["blood_pressure"] = df["blood_pressure"].astype(str)
df["blood_pressure"] = df["blood_pressure"].apply(
    lambda x: re.sub("[^0-9.]", "", x)
)
df["blood_pressure"] = df["blood_pressure"].astype(float)

# 3c. Risk level using lambda
df["risk_level"] = df.apply(
    lambda row: "High" if row["BMI"] > 30 and row["disease_score"] > 80
    else "Medium" if row["BMI"] > 25 and row["disease_score"] > 60
    else "Low",
    axis=1
)

# 3d. Groupby risk_level
risk_summary = df.groupby("risk_level")[["BMI", "disease_score"]].mean()
print(risk_summary)

# 3e. Visualisations
df.boxplot(column="BMI", by="risk_level")
plt.title("BMI by Risk Level")
plt.suptitle("")
plt.xlabel("Risk Level")
plt.ylabel("BMI")
plt.show()

df["age"].plot(kind="hist", bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
