import pandas as pd
import numpy as np

# Read CSV
df = pd.read_csv("../CSVs/Papers for reflection-Grid view.csv")

# Extract decisions and convert to arrays
alpha = df['alpha_decision'].map({'Yes': 1, 'No': 0}).values
beta = df['beta_decision'].map({'Yes': 1, 'No': 0}).values
gamma = df['gamma_decision'].map({'Yes': 1, 'No': 0}).values
delta = df['delta_decision'].map({'Yes': 1, 'No': 0}).values
epsilon = df['epsilon_decision'].map({'Yes': 1, 'No': 0}).values

# Create the formatted matrix string with exact formatting
matrix_str = """data = np.array([
    [{}],
    [{}],
    [{}],
    [{}],
    [{}]
])""".format(
    ','.join(map(str, alpha)),
    ','.join(map(str, beta)),
    ','.join(map(str, gamma)),
    ','.join(map(str, delta)),
    ','.join(map(str, epsilon))
).replace('[,', '[').replace(',]', ']')  # Clean up extra commas

# Print the matrix in the exact format needed
print(matrix_str)