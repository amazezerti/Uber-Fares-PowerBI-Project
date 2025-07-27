*Uber Fares Power BI Project 🚗💨
*📋 Project Overview
This repository contains the code, data, and visualizations for the Uber Fares Data Analysis Project, submitted as part of the Introduction to Big Data course at the Adventist University of Central Africa. The project analyzes the Uber Fares Dataset from Kaggle to uncover insights into ride fares, trip distances, temporal patterns, and geographic distribution. Using Python for preprocessing and Power BI for visualization, the project delivers an interactive dashboard to explore trends and provide actionable recommendations for Uber’s operations.
Student Details:

Name: Abdramane Mahamat Adji Zezerti
ID: 25718
Subject: Introduction to Big Data
Lecturer: Eric Maniraguha


🎯 Objectives
The project aims to:

🧹 Clean and preprocess the Uber Fares Dataset to ensure data quality.
🔍 Perform exploratory data analysis (EDA) to identify patterns in fares, distances, and ride times.
📊 Develop an interactive Power BI dashboard to visualize key metrics and trends.
💡 Provide recommendations to optimize Uber’s driver allocation and pricing strategies.


🛠 Methodology
1. Data Collection 📥

Source: Uber Fares Dataset from Kaggle (link).
Description: Contains ride details including fare_amount, pickup_datetime, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count.

2. Data Preprocessing 🧹

Tool: Python (Pandas, GeoPy) in Jupyter Notebook.
Steps:
Handled missing values: Imputed fare_amount with median (~$8.50), passenger_count with mode (1).
Removed invalid coordinates (latitude/longitude = 0.0).
Removed outliers in fare_amount using the Interquartile Range (IQR) method.
Engineered features: distance_miles (geodesic distance), hour, day_of_week, month, is_weekend, is_peak_hour (7-9 AM, 4-6 PM), fare_bin (fare quartiles).
Output: Cleaned dataset saved as uber_fares_cleaned.csv.



3. Exploratory Data Analysis (EDA) 📈

Tool: Python (Matplotlib, Seaborn).
Analyses:
Fare distribution: Histogram of fare_amount.
Fare vs. distance: Scatter plot of fare_amount vs. distance_miles.
Fare by hour: Line plot of average fare_amount by hour.


Output: Plots saved as fare_distribution.png, fare_vs_distance.png, fare_by_hour.png in /screenshots.

4. Power BI Dashboard 📊✨

Tool: Power BI Desktop.
Approach:
Imported uber_fares_cleaned.csv.
Used built-in aggregations (Average, Count) instead of DAX measures due to technical issues.
Created an interactive dashboard with visuals for KPIs, fare distribution, fare vs. distance, temporal patterns, and geographic distribution.
Added slicers for filtering by day_of_week, month, and is_peak_hour.




📂 Repository Structure
The repository contains the following files and folders:

📄 uber.csv: Raw dataset from Kaggle.
🐍 uber_data_preprocessing.py: Python script for cleaning and feature engineering.
🐍 uber_eda.py: Python script for generating EDA plots.
📄 uber_fares_cleaned.csv: Cleaned dataset used in Power BI.
📊 uber_fares_dashboard.pbix: Power BI dashboard file.
📝 Uber_Fares_Analysis_Report.md: Analytical report summarizing findings and recommendations.
📸 /screenshots: Folder containing screenshots named by operation:
data_import.png: Power BI Data view showing loaded dataset.
power_query.png: Power Query Editor showing data transformations.
dashboard.png: Final Power BI dashboard.
fare_distribution.png: EDA histogram of fare amounts.
fare_vs_distance.png: EDA scatter plot of fare vs. distance.
fare_by_hour.png: EDA line plot of average fare by hour.




🖼 Dashboard Features
The Power BI dashboard includes:

KPIs (Card Visuals) 📏:

Average Fare: Average of fare_amount (~$10.50).
Total Rides: Count of rides using key column.
Peak Hour Rides: Count of rides during peak hours (is_peak_hour = 1).


Fare Distribution (Clustered Column Chart) 📊:

Shows ride counts by fare_bin (Low, Mid-Low, Mid-High, High).
Highlights most fares are in the Low to Mid-Low range ($2.50–$10.00).


Fare vs. Distance (Scatter Plot) 📍:

Plots fare_amount vs. distance_miles, with ride count as bubble size.
Shows strong correlation (longer trips have higher fares).


Fare by Hour (Line Chart) ⏰:

Displays average fare_amount by hour.
Peaks at ~$12 during 7-9 AM and 4-6 PM.


Geographic Distribution (Map) 🌍:

Visualizes ride density using pickup_latitude and pickup_longitude.
Concentrated in Manhattan (~40.7°N, -73.9°E).


Busiest Periods (Bar Chart) 📅:

Shows ride counts by hour, with is_peak_hour as legend.
Highlights peak hours (7-9 AM, 4-6 PM) in red.


Slicers for Interactivity 🔎:

Filters for day_of_week, month, and is_peak_hour (dropdown style).
Allows dynamic exploration of trends (e.g., Fridays, peak hours).




🚀 Instructions to Run the Project

Clone the Repository:
git clone https://github.com/your-username/Uber-Fares-PowerBI-Project.git


Set Up Python Environment 🐍:

Install Anaconda: https://www.anaconda.com/products/distribution.
Install required libraries:pip install pandas numpy geopy matplotlib seaborn


Open Jupyter Notebook via Anaconda Navigator.


Run Preprocessing:

Open uber_data_preprocessing.py in Jupyter Notebook.
Ensure uber.csv is in the same folder.
Run the script to generate uber_fares_cleaned.csv.


Run EDA:

Open uber_eda.py in Jupyter Notebook.
Ensure uber_fares_cleaned.csv is available.
Run to generate plots (fare_distribution.png, etc.) in /screenshots.


View Dashboard:

Download Power BI Desktop: https://powerbi.microsoft.com/desktop/.
Open uber_fares_dashboard.pbix to explore the dashboard.
Alternatively, import uber_fares_cleaned.csv and recreate visuals (see Methodology).




📊 Key Findings

Fare Trends: Average fare is ~$10.50, with peaks at $12 during rush hours (7-9 AM, 4-6 PM).
Distance Correlation: Fares strongly correlate with distance_miles (r ≈ 0.70).
Temporal Patterns: Fridays and Saturdays have ~30% of total rides; peak hours account for ~25%.
Geographic Insights: Most rides occur in Manhattan, based on pickup coordinates.


💡 Recommendations

🚖 Driver Allocation: Deploy more drivers during peak hours (7-9 AM, 4-6 PM) and weekends to reduce wait times.
💸 Pricing Strategy: Optimize surge pricing for long-distance trips (>5 miles) to maximize revenue.
🗺 Geographic Focus: Prioritize driver availability in Manhattan to meet high demand.
📣 Marketing: Promote group rides (5–6 passengers) to increase ridership.


📸 Screenshots
All screenshots are named by the operation they represent and stored in the /screenshots folder:

Data Import: data_import.png (Power BI Data view).
Power Query: power_query.png (Power Query Editor).
Dashboard: dashboard.png (Final Power BI dashboard).
EDA Plots: fare_distribution.png, fare_vs_distance.png, fare_by_hour.png.


🙏 Acknowledgments

Kaggle: For providing the Uber Fares Dataset.
Lecturer Eric Maniraguha: For guidance in the Introduction to Big Data course.
Power BI Community: For resources on dashboard creation.


📝 Submission Details

Power BI File: uber_fares_dashboard.pbix (interactive dashboard).
Report: Uber_Fares_Analysis_Report.md (detailed analysis and recommendations).
GitHub Repository: https://github.com/your-username/Uber-Fares-PowerBI-Project (replace with your actual link).
Note: Submitted after the July 25, 2025 deadline (today is July 27, 2025, 5:50 PM CAT). Please contact Lecturer Eric Maniraguha at eric.maniraguha@auca.ac.rw to confirm late submission policies.


Author: Abdramane Mahamat Adji Zezerti (ID: 25718)Course: Introduction to Big DataDate: July 27, 2025Contact: Email Lecturer Eric Maniraguha at eric.maniraguha@auca.ac.rw for submission or queries.
