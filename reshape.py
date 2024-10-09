import pandas as pd

# Step 1: Read the CSV file into a pandas DataFrame
df = pd.read_csv('test/healthcare_staff.csv')

# Step 2: Use the pivot function to reshape the DataFrame
df_wide = df.pivot(index='date', columns=['state', 'type'], values='staff')

# Step 3: Save the reshaped DataFrame back to a CSV file if needed
df_wide.to_csv('test/healthcare_staff_wide.csv')

# Display the reshaped DataFrame
print(df_wide)