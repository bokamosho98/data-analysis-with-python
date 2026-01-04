import pandas as pd
import sqlite3

# Load cleaned data
df = pd.read_csv("../data/health_data.csv")

# Recreate risk_level
df["risk_level"] = df.apply(
    lambda row: "High" if row["BMI"] > 30 and row["disease_score"] > 80
    else "Medium" if row["BMI"] > 25 and row["disease_score"] > 60
    else "Low",
    axis=1
)

# 4a. Load into SQLite
conn = sqlite3.connect("../outputs/health_registry.db")
df.to_sql("patients", conn, if_exists="replace", index=False)

# 4b. Count patients by sex and risk level
query1 = """
SELECT sex, risk_level, COUNT(*) as count
FROM patients
GROUP BY sex, risk_level
"""
print(pd.read_sql(query1, conn))

# 4c. Average disease score per age group
query2 = """
SELECT
CASE
    WHEN age < 25 THEN 'Youth'
    WHEN age < 60 THEN 'Adult'
    ELSE 'Senior'
END AS age_group,
AVG(disease_score) as avg_disease_score
FROM patients
GROUP BY age_group
"""
print(pd.read_sql(query2, conn))

# 4d. CASE classification
query3 = """
SELECT *,
CASE
    WHEN disease_score > 80 THEN 'Critical'
    ELSE 'Stable'
END AS patient_status
FROM patients
"""
classified = pd.read_sql(query3, conn)
classified.to_csv("../outputs/patient_status.csv", index=False)

conn.close()
