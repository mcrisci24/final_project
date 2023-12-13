import pandas as pd

# Define the mapping of integers to month names
month_mapping = {
    "January": "Jan",
    "February": "Feb",
    "March": "Mar",
    "April": "Apr",
    "May": "May",
    "June": "Jun",
    "July": "Jul",
    "August": "Aug",
    "September": "Sep",
    "October": "Oct",
    "November": "Nov",
    "December": "Dec"
}

# Read the CSV file into a DataFrame
df = pd.read_csv("C:\\Users\\markc\\Downloads\\Airline_Delay_Cause_0_filtered.csv")

# Check how many rows in 'month' are NaN
print(f"Number of NaN values in month: {df['month'].isna().sum()}")

# Print rows where month is NOT NaN
print("\nRows where month is not NaN:")
print(df[df['month'].notna()].head())

# Map month numbers to names
df['month'] = df['month'].map(month_mapping)

print("\nAfter Mapping:")
print(df.head())
print(df.tail())
# Save the changes back to the CSV
df.to_csv("C:\\Users\\markc\\Downloads\\Airline_issues.csv", index=False)

