import pandas as pd

# Read the daily blood donations data
df = pd.read_csv('test/blood_donations_state.csv')

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Extract the year from the 'date' column
df['year'] = df['date'].dt.year

# Group by year, state, and blood type, and sum the donations
annual_df = df.groupby(['year', 'state', 'blood_type']).agg({'donations': 'sum'}).reset_index()

# Write the aggregated data to a new CSV file
annual_df.to_csv('test/annual_blood_donations.csv', index=False)

print("Annual blood donations data has been saved to 'annual_blood_donations.csv'")