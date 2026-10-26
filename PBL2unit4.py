import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Read sales2.csv
csv_path = Path(__file__).resolve().parent / "sales2.csv"

if not csv_path.exists():
    print("Error: sales2.csv file not found!")
    exit()

df = pd.read_csv(csv_path)

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Check required columns
required_columns = ["Month", "Category", "Sales"]

for col in required_columns:
    if col not in df.columns:
        print(f"Error: Missing column '{col}'")
        exit()

# Convert Sales to numeric
df["Sales"] = pd.to_numeric(
    df["Sales"].astype(str).str.replace(",", "", regex=False),
    errors="coerce"
)

# Remove invalid rows
df = df.dropna(subset=["Month", "Category", "Sales"])

if df.empty:
    print("Error: No valid sales data found!")
    exit()

print("\nSales Data:")
print(df)

# 2. Total and average sales
total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()

print("\nTotal Sales:", total_sales)
print("Average Sales:", round(average_sales, 2))

# 3. Monthly sales
month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

df["Month"] = df["Month"].astype(str).str.strip().str.title()

monthly_sales = df.groupby("Month")["Sales"].sum()

monthly_sales = monthly_sales.reindex(
    [month for month in month_order if month in monthly_sales.index]
)

highest_month = monthly_sales.idxmax()
highest_sales = monthly_sales.max()

print("\nMonth with Highest Sales:", highest_month)
print("Highest Sales:", highest_sales)

# 4. Category-wise sales
category_sales = df.groupby("Category")["Sales"].sum()

print("\nSales by Product Category:")
print(category_sales)

# 5. Bar chart
plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar", color="skyblue")

plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 6. Line chart
plt.figure(figsize=(9, 5))
monthly_sales.plot(
    kind="line",
    marker="o",
    color="green"
)

plt.title("Monthly Sales Trends")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# 7. Pie chart
if (category_sales >= 0).all() and category_sales.sum() > 0:
    plt.figure(figsize=(7, 7))
    category_sales.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Category Contribution to Total Sales")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()
else:
    print("Pie chart requires non-negative sales and a positive total.")

print("\nProgram Executed Successfully!")