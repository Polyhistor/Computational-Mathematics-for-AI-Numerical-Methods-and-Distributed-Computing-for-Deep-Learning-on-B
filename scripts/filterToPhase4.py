import pandas as pd

def filter_final_decision(input_csv, output_csv):
    """
    Filter CSV to keep only rows where final_decision is 1
    
    Parameters:
    input_csv (str): Path to input CSV file
    output_csv (str): Path to save filtered CSV file
    
    Returns:
    tuple: (total_rows, filtered_rows) counts
    """
    # Read the CSV file
    df = pd.read_csv(input_csv)
    
    # Filter rows where final_decision is 1
    filtered_df = df[df['final_decision'] == 1]
    
    # Save to new CSV file, maintaining exact structure
    filtered_df.to_csv(output_csv, index=False)
    
    return len(df), len(filtered_df)


total, filtered = filter_final_decision('./../CSVs/export - Phase 3_ Quality Screening.csv', 'filtered_output.csv')
print(f"Total rows: {total}")
print(f"Rows with final_decision = 1: {filtered}")