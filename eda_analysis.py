import pandas as pd

# Load dataset
df = pd.read_excel("Dataset for Data Analytics.xlsx")

# -----------------------------
# Basic Information
# -----------------------------
print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

# -----------------------------
# Basic Statistics
# -----------------------------
print("\nDescriptive Statistics:")
print(df.describe())

# Mean, Median and Count
numeric_columns = ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]

print("\nMean:")
print(df[numeric_columns].mean())

print("\nMedian:")
print(df[numeric_columns].median())

print("\nCount:")
print(df[numeric_columns].count())

# -----------------------------
# Outlier Detection (IQR Method)
# -----------------------------
print("\nOutliers:")

for col in numeric_columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower) | (df[col] > upper)]

    print(f"{col}: {len(outliers)} outliers")

# -----------------------------
# Trends
# -----------------------------
print("\nProduct Frequency:")
print(df["Product"].value_counts())

print("\nPayment Method Frequency:")
print(df["PaymentMethod"].value_counts())

print("\nOrder Status:")
print(df["OrderStatus"].value_counts())

print("\nReferral Source:")
print(df["ReferralSource"].value_counts())
