import pandas as pd

# Step 1: Read the CSV file
df = pd.read_csv('heatmap/organ_pledges_state.csv')

# Step 2: Convert the date column to datetime
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# Step 3: Extract year and month from the date column
df['year_month'] = df['date'].dt.to_period('M')

# Step 4: Group by state and year_month, then sum the pledges
monthly_df = df.groupby(['state', 'year_month'])['pledges'].sum().reset_index()

# Step 5: Convert the year_month back to a datetime format for better readability
monthly_df['year_month'] = monthly_df['year_month'].dt.to_timestamp()

# Step 6: Save the new DataFrame to a CSV file
monthly_df.to_csv('heatmap/monthly_organ_pledges.csv', index=False)