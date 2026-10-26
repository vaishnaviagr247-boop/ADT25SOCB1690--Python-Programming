import pandas as pd
from pathlib import Path

def load_sales_data():
    csv_path = Path("sales.csv")

    if not csv_path.exists():
        data = {
            'Product': ['Laptop', 'Mouse', 'Laptop', 'Keyboard', 'Monitor'],
            'Quantity': [3, 15, 2, 8, 4],
            'Price': [1200, 25, 1250, 75, 200]
        }

        df = pd.DataFrame(data)
        df.to_csv(csv_path, index=False)

    return pd.read_csv(csv_path)


def main():
    df = load_sales_data()

    # Remove extra spaces from column names
    df.columns = df.columns.str.strip()

    # Convert Quantity and Price into numbers
    df['Quantity'] = pd.to_numeric(
        df['Quantity'].astype(str).str.replace(',', ''),
        errors='coerce'
    )

    df['Price'] = pd.to_numeric(
        df['Price'].astype(str).str.replace(',', ''),
        errors='coerce'
    )

    # Remove invalid values
    df = df.dropna(subset=['Quantity', 'Price'])

    # Calculate total sales
    df['Total_Sales'] = df['Quantity'] * df['Price']

    # Group sales by product
    result = df.groupby('Product', as_index=False)['Total_Sales'].sum()

    print("Total Sales Report:")
    print(result.to_string(index=False))


if __name__ == "__main__":
    main()