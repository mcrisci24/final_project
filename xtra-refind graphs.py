import pandas as pd
import geopandas as gpd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the filtered data
df = pd.read_csv("C:\\Users\\markc\\Downloads\\Airline_Delay_Cause_0_filtered.csv")

# Make sure 'month' is of type string for plotting
df['month'] = df['month'].astype(str)

# Select only the numeric columns for correlation analysis
numeric_columns = [
    'arr_del15', 'carrier_ct', 'weather_ct', 'nas_ct', 'security_ct',
    'late_aircraft_ct', 'arr_cancelled', 'arr_diverted', 'arr_delay',
    'carrier_delay', 'weather_delay', 'nas_delay', 'security_delay', 'late_aircraft_delay'
]

# Calculate the correlation matrix
'''corr_matrix = df[numeric_columns].corr()

# Mask to avoid repeated values and diagonal
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

# Find the 30 highest correlations (excluding the diagonal)
corr_unstacked = corr_matrix.mask(mask).unstack().sort_values(kind="quicksort", ascending=False).dropna()
top_30_pairs = corr_unstacked.head(30)

# Now we have the top 30 correlations, let's plot them against months
for (var1, var2), corr_value in top_30_pairs.items():
    # Create a new DataFrame for each pair with months, var1, and var2
    monthly_data = df[['month', var1, var2]].groupby('month').mean().reset_index()

    # Line Plot
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=monthly_data, x='month', y=var1, marker='o', label=var1)
    sns.lineplot(data=monthly_data, x='month', y=var2, marker='o', label=var2)
    plt.title(f'Average Monthly Trend for {var1} vs {var2} (Correlation: {corr_value:.2f})')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Bar Plot
    monthly_data_melted = pd.melt(monthly_data, id_vars='month', value_vars=[var1, var2])
    plt.figure(figsize=(14, 7))
    sns.barplot(data=monthly_data_melted, x='month', y='value', hue='variable')
    plt.title(f'Average Monthly {var1} and {var2} (Correlation: {corr_value:.2f})')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Histogram Plot
    plt.figure(figsize=(14, 7))
    sns.histplot(df, x=var1, kde=True, color='blue', label=var1)
    sns.histplot(df, x=var2, kde=True, color='orange', label=var2)
    plt.title(f'Distribution of {var1} and {var2}')
    plt.legend()
    plt.tight_layout()
    plt.show()

'''
# Load the filtered data
df = pd.read_csv("C:\\Users\\markc\\Downloads\\Airline_Delay_Cause_0_filtered.csv")

# Make sure 'month' is of type string for plotting
df['month'] = df['month'].astype(str)

# Select only the numeric columns for correlation analysis
numeric_columns = [
    'arr_del15', 'carrier_ct', 'weather_ct', 'nas_ct', 'security_ct',
    'late_aircraft_ct', 'arr_cancelled', 'arr_diverted', 'arr_delay',
    'carrier_delay', 'weather_delay', 'nas_delay', 'security_delay', 'late_aircraft_delay'
]

# Calculate the correlation matrix
''''corr_matrix = df[numeric_columns].corr()

# Mask to avoid repeated values and diagonal
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

# Find the 30 highest correlations (excluding the diagonal)
corr_unstacked = corr_matrix.mask(mask).unstack().sort_values(kind="quicksort", ascending=False).dropna()
top_30_pairs = corr_unstacked.head(30)

# Now we have the top 30 correlations, let's plot them against months
for (var1, var2), corr_value in top_30_pairs.items():
    # Create a new DataFrame for each pair with months, var1, and var2
    monthly_data = df[['month', var1, var2]].groupby('month').mean().reset_index()

    # Line Plot
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=monthly_data, x='month', y=var1, marker='o', label=var1)
    sns.lineplot(data=monthly_data, x='month', y=var2, marker='o', label=var2)
    plt.title(f'Average Monthly Trend for {var1} vs {var2} (Correlation: {corr_value:.2f})')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Bar Plot
    monthly_data_melted = pd.melt(monthly_data, id_vars='month', value_vars=[var1, var2])
    plt.figure(figsize=(14, 7))
    sns.barplot(data=monthly_data_melted, x='month', y='value', hue='variable')
    plt.title(f'Average Monthly {var1} and {var2} (Correlation: {corr_value:.2f})')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Histogram Plot
    plt.figure(figsize=(14, 7))
    sns.histplot(df, x=var1, kde=True, color='blue', label=var1)
    sns.histplot(df, x=var2, kde=True, color='orange', label=var2)
    plt.title(f'Distribution of {var1} and {var2}')
    plt.legend()
    plt.tight_layout()
    plt.show()
'''
# Load the new dataset provided by the user
file_path_new = '/mnt/data/Airline_Delay_Cause_0_filtered.csv'
airline_data_new = pd.read_csv(file_path_new)

# Display the first few rows of the new dataset to understand its structure
airline_data_new.head()


# Manually mapping the dataset airport names to the correct GPS coordinates
# This approach will ensure accuracy in mapping

# Correct airport names as they appear in the dataset
correct_airport_names = {
    "Orlando, FL: Orlando International": gpd["Orlando International Airport"],
    "Fort Myers, FL: Southwest Florida International": gpd["Southwest Florida International Airport"],
    "Sarasota/Bradenton, FL: Sarasota/Bradenton International": gpd["Sarasota/Bradenton International Airport"],
    # Adding mappings for Tampa International and St. Petersburg/Clearwater International if they exist in the dataset
    "Tampa, FL: Tampa International": gpd.get("Tampa International Airport"),
    "St. Petersburg/Clearwater, FL: St. Petersburg/Clearwater International": gpd.get("St. Petersburg/Clearwater International Airport")
}

# Filtering the dataset for the specific airports and assigning GPS coordinates
selected_airports_data_corrected = airline_data_new[airline_data_new['airport_name'].isin(correct_airport_names.keys())]
selected_airports_data_corrected['gps_coordinates'] = selected_airports_data_corrected['airport_name'].map(correct_airport_names)

selected_airports_data_corrected.head()

# Assigning the modified dataset with GPS coordinates to a new variable
# This will keep the original dataset unchanged

modified_airline_data = selected_airports_data_corrected

# The original dataset remains in 'airline_data_new'
# The modified dataset with GPS coordinates is now in 'modified_airline_data'

# Displaying the first few rows of the modified dataset to confirm
modified_airline_data.head()

# Adding the mapping for St. Petersburg/Clearwater International Airport
correct_airport_names["St. Petersburg, FL: St Pete Clearwater International"] = gpd["St. Petersburg/Clearwater International Airport"]

# Re-filtering the dataset for the specific airports with the updated mapping
selected_airports_data_corrected_update = airline_data_new[airline_data_new['airport_name'].isin(correct_airport_names.keys())]
selected_airports_data_corrected_update['gps_coordinates'] = selected_airports_data_corrected_update['airport_name'].map(correct_airport_names)

selected_airports_data_corrected_update.head()
