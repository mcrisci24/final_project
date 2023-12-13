import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the filtered data
df = pd.read_csv("C:\\Users\\markc\\Downloads\\Airline_Delay_Cause_0_filtered.csv")

# Select only the numeric columns for correlation analysis
numeric_columns = [
    'arr_del15', 'carrier_ct', 'weather_ct', 'nas_ct', 'security_ct',
    'late_aircraft_ct', 'arr_cancelled', 'arr_diverted', 'arr_delay',
    'carrier_delay', 'weather_delay', 'nas_delay', 'security_delay', 'late_aircraft_delay'
]



# List of major airports in the specified states and cities
# Replace these with the actual names from your dataset
major_airports = [
    'Dallas/Fort Worth, TX: Dallas/Fort Worth International', 'Denver, CO: Denver International',
    'Los Angeles, CA: Los Angeles International', 'San Francisco, CA: San Francisco International',
    'Seattle, WA: Seattle/Tacoma International', 'Washington, DC: Washington Dulles International',
    'Philadelphia, PA: Philadelphia International', 'New York, NY: John F. Kennedy International',
    'Boston, MA: Logan International', 'Chicago, IL: Chicago O\'Hare International',
    'Charlotte, NC: Charlotte Douglas International'
]

# Filter the dataframe for these airports
df_filtered = df[df['airport_name'].isin(major_airports)]

# Calculate correlation matrix for the numeric columns related to delays
numeric_columns = [
    'arr_del15', 'carrier_ct', 'weather_ct', 'nas_ct', 'security_ct',
    'late_aircraft_ct', 'arr_cancelled', 'arr_diverted', 'arr_delay',
    'carrier_delay', 'weather_delay', 'nas_delay', 'security_delay',
    'late_aircraft_delay'
]


corr_matrix = df_filtered[numeric_columns].corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Matrix of Airline Delay Variables")
plt.show()

# Print the top 5 correlations
flat_corr_matrix = corr_matrix.unstack().sort_values(kind="quicksort", ascending=False)
strongest_pairs = flat_corr_matrix[flat_corr_matrix < 1].drop_duplicates()
print("Top 5 Pairs with Strongest Correlation:")
print(strongest_pairs.head(10))

# Analyze mean delays for the airports
mean_delays = df_filtered.groupby('airport_name')[numeric_columns].mean()
print("\nMean Delay Metrics for Major Airports in Specified States and Cities:")
print(mean_delays)

# Optionally, save the filtered data to a new CSV for further analysis
df_filtered.to_csv("C:\\Users\\markc\\Downloads\\Airline_Delay_Causes_Major.csv", index=False)

# Calculate the correlation matrix
corr_matrix = df[numeric_columns].corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Matrix of Airline Delay Variables")
plt.show()

# Identify the pairs with the strongest positive or negative correlation
strongest_pairs = corr_matrix.unstack().sort_values(kind="quicksort", ascending=False)
strongest_pairs = strongest_pairs[strongest_pairs < 1]  # Exclude the diagonal (correlation of 1 with themselves)
print("Top 5 Pairs with Strongest Correlation:")
print(strongest_pairs.head(10))  # Each pair is listed twice, AB and BA, hence head(10) to get the top 5 unique pairs


# Define the list of airports to analyze
airports = [
    "Sarasota/Bradenton, FL: Sarasota/Bradenton International",
    "Tampa, FL: Tampa International",
    "St. Petersburg, FL: St Pete Clearwater International",
    "Fort Myers, FL: Southwest Florida International",
    "Orlando, FL: Orlando International"
]

# Filter the DataFrame to only include the specified airports
df_filtered = df[df['airport_name'].isin(airports)]

# Select only the numeric columns for correlation analysis
numeric_columns = [
    'arr_del15', 'carrier_ct', 'weather_ct', 'nas_ct', 'security_ct',
    'late_aircraft_ct', 'arr_cancelled', 'arr_diverted', 'arr_delay',
    'carrier_delay', 'weather_delay', 'nas_delay', 'security_delay', 'late_aircraft_delay'
]

# Calculate the correlation matrix
corr_matrix = df_filtered[numeric_columns].corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Matrix of Airline Delay Variables")
plt.show()

# Aggregate the total counts for each type of delay/cancellation for each airport
airport_issues = df_filtered.groupby('airport_name')[numeric_columns].sum()

# Add a total issues column to sum all types of issues
airport_issues['total_issues'] = airport_issues.sum(axis=1)

# Rank the airports based on total issues
airport_ranking = airport_issues.sort_values(by='total_issues', ascending=True)

# Plot the total issues for each airport
plt.figure(figsize=(12, 6))
airport_ranking['total_issues'].plot(kind='barh', color='skyblue')
plt.title("Total Travel Issues by Airport")
plt.xlabel("Total Issues Count")
plt.ylabel("Airport")
plt.show()

# Print the ranked list of airports
print("Airports Ranked by Easiest to Travel To/From Based on Total Issues:")
print(airport_ranking.index.tolist())

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the filtered data
df = pd.read_csv("C:\\Users\\markc\\Downloads\\Airline_Delay_Cause_0_filtered.csv")

# Select only the numeric columns for correlation analysis
numeric_columns = [
    'arr_del15', 'carrier_ct', 'weather_ct', 'nas_ct', 'security_ct',
    'late_aircraft_ct', 'arr_cancelled', 'arr_diverted', 'arr_delay',
    'carrier_delay', 'weather_delay', 'nas_delay', 'security_delay', 'late_aircraft_delay'
]



# List of major airports in the specified states and cities
# Replace these with the actual names from your dataset
major_airports = [
    'Dallas/Fort Worth, TX: Dallas/Fort Worth International', 'Denver, CO: Denver International',
    'Los Angeles, CA: Los Angeles International', 'San Francisco, CA: San Francisco International',
    'Seattle, WA: Seattle/Tacoma International', 'Washington, DC: Washington Dulles International',
    'Philadelphia, PA: Philadelphia International', 'New York, NY: John F. Kennedy International',
    'Boston, MA: Logan International', 'Chicago, IL: Chicago O\'Hare International',
    'Charlotte, NC: Charlotte Douglas International'
]

# Filter the dataframe for these airports
df_filtered = df[df['airport_name'].isin(major_airports)]

# Calculate correlation matrix for the numeric columns related to delays
numeric_columns = [
    'arr_del15', 'carrier_ct', 'weather_ct', 'nas_ct', 'security_ct',
    'late_aircraft_ct', 'arr_cancelled', 'arr_diverted', 'arr_delay',
    'carrier_delay', 'weather_delay', 'nas_delay', 'security_delay',
    'late_aircraft_delay'
]


corr_matrix = df_filtered[numeric_columns].corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Matrix of Airline Delay Variables")
plt.show()

# Print the top 5 correlations
flat_corr_matrix = corr_matrix.unstack().sort_values(kind="quicksort", ascending=False)
strongest_pairs = flat_corr_matrix[flat_corr_matrix < 1].drop_duplicates()
print("Top 5 Pairs with Strongest Correlation:")
print(strongest_pairs.head(10))

# Analyze mean delays for the airports
mean_delays = df_filtered.groupby('airport_name')[numeric_columns].mean()
print("\nMean Delay Metrics for Major Airports in Specified States and Cities:")
print(mean_delays)

# Optionally, save the filtered data to a new CSV for further analysis
df_filtered.to_csv("C:\\Users\\markc\\Downloads\\Airline_Delay_Causes_Major.csv", index=False)

# Calculate the correlation matrix
corr_matrix = df[numeric_columns].corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Matrix of Airline Delay Variables")
plt.show()

# Identify the pairs with the strongest positive or negative correlation
strongest_pairs = corr_matrix.unstack().sort_values(kind="quicksort", ascending=False)
strongest_pairs = strongest_pairs[strongest_pairs < 1]  # Exclude the diagonal (correlation of 1 with themselves)
print("Top 5 Pairs with Strongest Correlation:")
print(strongest_pairs.head(10))  # Each pair is listed twice, AB and BA, hence head(10) to get the top 5 unique pairs


# Define the list of airports to analyze
airports = [
    "Sarasota/Bradenton, FL: Sarasota/Bradenton International",
    "Tampa, FL: Tampa International",
    "St. Petersburg, FL: St Pete Clearwater International",
    "Fort Myers, FL: Southwest Florida International",
    "Orlando, FL: Orlando International"
]

# Filter the DataFrame to only include the specified airports
df_filtered = df[df['airport_name'].isin(airports)]

# Select only the numeric columns for correlation analysis
numeric_columns = [
    'arr_del15', 'carrier_ct', 'weather_ct', 'nas_ct', 'security_ct',
    'late_aircraft_ct', 'arr_cancelled', 'arr_diverted', 'arr_delay',
    'carrier_delay', 'weather_delay', 'nas_delay', 'security_delay', 'late_aircraft_delay'
]

# Calculate the correlation matrix
corr_matrix = df_filtered[numeric_columns].corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Matrix of Airline Delay Variables")
plt.show()

# Aggregate the total counts for each type of delay/cancellation for each airport
airport_issues = df_filtered.groupby('airport_name')[numeric_columns].sum()

# Add a total issues column to sum all types of issues
airport_issues['total_issues'] = airport_issues.sum(axis=1)

# Rank the airports based on total issues
airport_ranking = airport_issues.sort_values(by='total_issues', ascending=True)

# Plot the total issues for each airport
plt.figure(figsize=(12, 6))
airport_ranking['total_issues'].plot(kind='barh', color='skyblue')
plt.title("Total Travel Issues by Airport")
plt.xlabel("Total Issues Count")
plt.ylabel("Airport")
plt.show()

# Print the ranked list of airports
print("Airports Ranked by Easiest to Travel To/From Based on Total Issues:")
print(airport_ranking.index.tolist())

