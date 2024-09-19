import pandas as pd
import numpy as np

def clean_csv(input_file, output_file, columns_to_clean=None):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    print(f"Original shape: {df.shape}")
    print(f"Columns in the DataFrame: {df.columns.tolist()}")  # Print column names

    # If specific columns are provided, only clean those
    if columns_to_clean:
        columns_to_process = columns_to_clean
    else:
        # Only process numeric columns
        columns_to_process = df.select_dtypes(include=[np.number]).columns

    # Remove outliers
    for column in columns_to_process:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

    print(f"Shape after removing outliers: {df.shape}")

    # Check if 'Name' column exists
    if 'Name' in df.columns:  # Change 'title' to 'Name' or any other column you want to use
        # After reading the CSV file and before removing duplicates
        duplicate_names = df[df.duplicated(subset='Name', keep=False)]  # Find all duplicates in the 'Name' column
        total_duplicates = duplicate_names.shape[0]  # Count total number of duplicate entries

        if total_duplicates > 0:
            print(f"Total number of duplicate names found: {total_duplicates}")
            print(duplicate_names)
        else:
            print("No duplicate names found.")

        # Remove duplicates based on the 'Name' column only
        df.drop_duplicates(subset='Name', inplace=True)
        print(f"Final shape after removing duplicates: {df.shape}")
    else:
        print("Error: 'Name' column not found in the DataFrame.")

    # Save the cleaned data to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    input_file = "../CSVs/Phase 1_ Study Collection-Grid view.csv"
    output_file = "cleaned_output.csv"
    # Optionally, specify columns to clean. If not provided, all numeric columns will be processed.
    # columns_to_clean = ["column1", "column2"]
    
    clean_csv(input_file, output_file)
    # If you want to clean specific columns, uncomment the following line and specify the columns:
    # clean_csv(input_file, output_file, columns_to_clean)