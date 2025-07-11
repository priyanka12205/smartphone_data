import pandas as pd

# Load CSV file
df = pd.read_csv('Smartphones_cleaned_dataset.csv')

# Keep only the relevant columns
df = df[['brand_name', 'model', 'price', 'rating', 'has_5g', 'ram_capacity', 'internal_memory', 'battery_capacity']]

# Convert price from INR to USD (approx conversion)
df['price_usd'] = df['price'] / 83
df['price_usd'] = df['price_usd'].round(2)

# Filter smartphones with rating >= 85 and 5G support
df_filtered = df[(df['rating'] >= 85) & (df['has_5g'] == True)]

# Sort by rating descending
df_sorted = df_filtered.sort_values(by='rating', ascending=False)

# Save to new CSV
df_sorted.to_csv('Smartphones_transformed.csv', index=False)

print("Transformation complete. File saved as 'Smartphones_transformed.csv'.")
