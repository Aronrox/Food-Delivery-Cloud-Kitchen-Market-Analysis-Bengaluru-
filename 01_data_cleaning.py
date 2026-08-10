import pandas as pd
import numpy as np

def clean_food_data(file_path):
    print("Loading data...")
    df = pd.read_csv(file_path)
    
    print("Starting data cleaning pipeline...")
    # 1. Drop unnecessary columns to reduce memory usage
    columns_to_drop = ['url', 'phone', 'dish_liked']
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])
    
    # 2. Clean the 'rate' column (e.g., convert '4.1/5' string to 4.1 float)
    df['rate'] = df['rate'].astype(str)
    df['rate'] = df['rate'].apply(lambda x: x.replace('/5', '').strip())
    df['rate'] = pd.to_numeric(df['rate'], errors='coerce')
    
    # 3. Clean the cost column (e.g., convert '1,200' string to 1200 integer)
    if 'approx_cost(for two people)' in df.columns:
        df = df.rename(columns={'approx_cost(for two people)': 'cost_for_two'})
        df['cost_for_two'] = df['cost_for_two'].astype(str).apply(lambda x: x.replace(',', ''))
        df['cost_for_two'] = pd.to_numeric(df['cost_for_two'], errors='coerce')
    
    # 4. Handle Missing Values
    # Impute missing ratings with the median, drop rows entirely missing location data
    df['rate'] = df['rate'].fillna(df['rate'].median())
    df = df.dropna(subset=['location', 'cuisines'])
    
    # 5. Feature Engineering: Standardize Cuisines targeting our business case
    df['is_tandoori_biryani'] = df['cuisines'].str.contains('Biryani|Tandoori', case=False, na=False)
    df['is_dessert_bakery'] = df['cuisines'].str.contains('Dessert|Bakery|Cake', case=False, na=False)
    
    print("Cleaning complete. Saving to processed folder...")
    df.to_csv('data/cleaned_zomato_data.csv', index=False)
    return df

if __name__ == "__main__":
    # Replace with your downloaded dataset path
    clean_food_data('data/zomato.csv')
