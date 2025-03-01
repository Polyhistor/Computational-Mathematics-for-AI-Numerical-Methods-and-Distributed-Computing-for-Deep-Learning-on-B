import pandas as pd

# Read the existing CSV
df = pd.read_csv("./../CSVs/export - Phase 3_ Quality Screening - Grid.csv")

# Add quality assessment columns for each reviewer (alpha through epsilon)

criteria = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7']

# Create new columns for each reviewer and criterion
for criterion in criteria:
    column_name = f"{criterion}"
    df[column_name] = ""  # Empty string for Yes/No input


df['final_decision'] = ""

# Save the updated CSV
df.to_csv("./../CSVs/quality_assessment_grid.csv", index=False)