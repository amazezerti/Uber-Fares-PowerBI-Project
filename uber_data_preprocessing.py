import pandas as pd
import numpy as np
from geopy.distance import geodesic
from datetime import datetime

# Load the dataset
df = pd.read_csv('uber.csv')

# Step 1: Data Understanding
print("Dataset Structure:")
print(df.info())
print("\nDataset Dimensions:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())

# Step 2: Data Cleaning
# Handle missing values
df['fare_amount'] = df['fare_amount'].fillna(df['fare_amount'].median())
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], errors='coerce')
df = df.dropna(subset=['pickup_datetime'])
df['passenger_count'] = df['passenger_count'].fillna(df['passenger_count'].mode()[0])

# Remove invalid coordinates (latitude/longitude = 0.0)
df = df[(df['pickup_longitude'] != 0.0) & (df['pickup_latitude'] != 0.0) &
        (df['dropoff_longitude'] != 0.0) & (df['dropoff_latitude'] != 0.0)]

# Remove outliers in fare_amount using IQR
Q1 = df['fare_amount'].quantile(0.25)
Q3 = df['fare_amount'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['fare_amount'] >= Q1 - 1.5 * IQR) & (df['fare_amount'] <= Q3 + 1.5 * IQR)]

# Step 3: Feature Engineering
# Calculate trip distance using geodesic distance
def calculate_distance(row):
    try:
        return geodesic(
            (row['pickup_latitude'], row['pickup_longitude']),
            (row['dropoff_latitude'], row['dropoff_longitude'])
        ).miles
    except:
        return np.nan

df['distance_miles'] = df.apply(calculate_distance, axis=1)
df['distance_miles'] = df['distance_miles'].fillna(df['distance_miles'].median())

# Extract temporal features
df['hour'] = df['pickup_datetime'].dt.hour
df['day_of_week'] = df['pickup_datetime'].dt.day_name()
df['month'] = df['pickup_datetime'].dt.month_name()
df['is_weekend'] = df['day_of_week'].isin(['Saturday', 'Sunday']).astype(int)
df['is_peak_hour'] = df['hour'].isin([7, 8, 9, 16, 17, 18]).astype(int)

# Bin fare_amount into quartiles
df['fare_bin'] = pd.qcut(df['fare_amount'], q=4, labels=['Low', 'Mid-Low', 'Mid-High', 'High'])

# Save cleaned dataset
df.to_csv('uber_fares_cleaned.csv', index=False)
print("Cleaned dataset saved as 'uber_fares_cleaned.csv'")