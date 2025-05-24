import pandas as pd
import numpy as np
import os

def load_data(filepath):
    return pd.read_csv(filepath)

def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df['product'] = df['product'].fillna('Unknown')
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    df['quantity'] = df['quantity'].fillna(1)

    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['price'] = df['price'].fillna(df['price'].mean())

    df['customer_id'] = df['customer_id'].fillna(0).astype(int)

    # Standardize date formats
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    return df

def save_clean_data(df, output_path):
    df.to_csv(output_path, index=False)

if __name__ == '__main__':
    input_path = 'data/raw/customer_sales_raw.csv'
    output_path = 'data/cleaned/customer_sales_cleaned.csv'

    df = load_data(input_path)
    df_clean = clean_data(df)
    save_clean_data(df_clean, output_path)
    print(f"Cleaned data saved to {output_path}")

