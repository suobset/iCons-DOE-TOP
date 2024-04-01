import pandas as pd

# Assuming your dataset is in a CSV file named 'your_dataset.csv'
df = pd.read_csv('../data/main/all_ODIN_3.csv')

# Filter entries where STATE is Minnesota
minnesota_data = df[df['STATE'] == 'Minnesota']

# Calculate the range of F_VALUE
f_value_range = minnesota_data['F_VALUE'].min(), minnesota_data['F_VALUE'].max()

print(f"{f_value_range}")
