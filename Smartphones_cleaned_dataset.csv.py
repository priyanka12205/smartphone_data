import pandas as pd

# Input and Output paths
input_path = r'C:\Users\yarla\Downloads\Student_Data\Student_performance_data.csv'
output_path = r'C:\Users\yarla\Downloads\Student_Data\Student_cleaned_data.csv'

try:
    # Load the dataset
    df = pd.read_csv(input_path)
    print("Original data loaded successfully!")

    # --- Cleaning and Transforming ---
    df_cleaned = df.dropna()
    df_cleaned.columns = [col.strip().lower().replace(" ", "_") for col in df_cleaned.columns]

    for col in df_cleaned.select_dtypes(include='object'):
        df_cleaned[col] = df_cleaned[col].str.strip().str.title()

    # Save the cleaned data
    df_cleaned.to_csv(output_path, index=False)
    print(f"\nCleaned data saved to: {output_path}")

    # Show cleaned data in terminal
    print("\n📊 Cleaned Data Preview:")
    print(df_cleaned.head(10))  # Show first 10 rows
    print(f"\nTotal rows after cleaning: {len(df_cleaned)}")

except FileNotFoundError:
    print(f"❌ File not found at: {input_path}")
except Exception as e:
    print(f"❌ An error occurred: {e}")
