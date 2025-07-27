import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv('uber_fares_cleaned.csv')

# Descriptive Statistics
print("\nDescriptive Statistics:\n", df.describe())
print("\nFare Amount by Day of Week:\n", df.groupby('day_of_week')['fare_amount'].mean())
print("\nFare Amount by Hour:\n", df.groupby('hour')['fare_amount'].mean())

# Plot 1: Fare Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['fare_amount'], bins=30, kde=True)
plt.title('Distribution of Fare Amount')
plt.xlabel('Fare Amount ($)')
plt.ylabel('Frequency')
plt.savefig('fare_distribution.png')
plt.close()

# Plot 2: Fare vs. Distance
plt.figure(figsize=(10, 6))
sns.scatterplot(x='distance_miles', y='fare_amount', data=df)
plt.title('Fare Amount vs. Distance')
plt.xlabel('Distance (miles)')
plt.ylabel('Fare Amount ($)')
plt.savefig('fare_vs_distance.png')
plt.close()

# Plot 3: Fare by Hour
hourly_fares = df.groupby('hour')['fare_amount'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.lineplot(x='hour', y='fare_amount', data=hourly_fares)
plt.title('Average Fare by Hour of Day')
plt.xlabel('Hour')
plt.ylabel('Average Fare ($)')
plt.savefig('fare_by_hour.png')
plt.close()

print("Plots saved as fare_distribution.png, fare_vs_distance.png, fare_by_hour.png")