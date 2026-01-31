import pandas as pd

def load_data():
    df = pd.read_csv("data/transactions.csv")
    df.columns = df.columns.str.strip()

    df = df[['Customer ID', 'StockCode', 'Quantity', 'Price']]
    df.dropna(inplace=True)

    df['Total'] = df['Quantity'] * df['Price']

    print(f"Processed {len(df)} transactions")
    return df
