# 🚗💨 **Uber Fares Power BI Project**

## 📋 **Project Overview**

This repository contains code, data, and visualizations for an exploratory analysis of Uber ride fares. I used a Kaggle dataset to uncover insights around pricing, trip distances, time-based patterns, and geographic distribution. Python was used for data preparation, and Power BI helped bring the findings to life through interactive dashboards. The goal is to better understand ride behavior and suggest ideas that could improve operational efficiency.

**_Student Details:_**
- **Name:** Abdramane Mahamat Adji Zezerti  
- **ID:** 25718  
- **Subject:** Introduction to Big Data  
- **Lecturer:** Eric Maniraguha  

---

## 🎯 **Objectives**

The project aims to:

- 🧹 Clean and preprocess the Uber Fares Dataset to ensure data quality.  
- 🔍 Perform exploratory data analysis (EDA) to identify patterns in fares, distances, and ride times.  
- 📊 Develop an interactive Power BI dashboard to visualize key metrics and trends.  
- 💡 Provide recommendations to optimize Uber’s driver allocation and pricing strategies.

---

## 🛠 **Methodology**

### 1. _Data Collection_ 📥  
- **Source:** Uber Fares Dataset from Kaggle  
- **Description:** Contains ride details including:
  - `fare_amount`  
  - `pickup_datetime`  
  - `pickup_longitude`, `pickup_latitude`  
  - `dropoff_longitude`, `dropoff_latitude`  
  - `passenger_count`  

---

### 2. _Data Preprocessing_ 🧹  
- **Tool:** Python (Pandas, GeoPy)  
- **Steps:**
  - Imputed missing `fare_amount` with median (~$8.50)  
  - Imputed `passenger_count` with mode (1)  
  - Removed invalid coordinates (`latitude/longitude = 0.0`)  
  - Removed outliers using the IQR method  
  - Engineered features:
    - `distance_miles`, `hour`, `day_of_week`, `month`  
    - `is_weekend`, `is_peak_hour`, `fare_bin`  
- **Output:** `uber_fares_cleaned.csv`  

---

### 3. _Exploratory Data Analysis (EDA)_ 📈  
- **Tool:** Python (Matplotlib, Seaborn)  
- **Analyses:**
  - Histogram of `fare_amount`  
  - Scatter plot of `fare_amount` vs. `distance_miles`  
  - Line plot of average `fare_amount` by hour  
- **Output:**  
  Plots saved as `.png` files in `/screenshots` folder

---

### 4. _Power BI Dashboard_ 📊✨  
- **Tool:** Power BI Desktop  
- **Approach:**
  - Imported `uber_fares_cleaned.csv`  
  - Used built-in aggregations (Average, Count)  
  - Created visuals for KPIs, fare patterns, and maps  
  - Added slicers for filtering by:
    - `day_of_week`, `month`, `is_peak_hour`

---

## 📂 **Repository Structure**

- 📄 `uber.csv` – Raw dataset  
- 🐍 `uber_data_preprocessing.py` – Python preprocessing script  
- 🐍 `uber_eda.py` – Python script for generating plots  
- 📄 `uber_fares_cleaned.csv` – Cleaned dataset  
- 📊 `uber_fares_dashboard.pbix` – Power BI dashboard file  
- 📝 `Uber_Fares_Analysis_Report.md` – Summary report  
- 📸 `/screenshots` – Folder containing:
  - `data_import.png`, `power_query.png`, `dashboard.png`  
  - `fare_distribution.png`, `fare_vs_distance.png`, `fare_by_hour.png`  

---

## 🖼 **Dashboard Features**

### KPIs (Card Visuals) 📏  
- **Average Fare:** ~$10.50  
- **Total Rides:** Count from `key` column  
- **Peak Hour Rides:** Count where `is_peak_hour = 1`  

### Fare Distribution 📊  
- Clustered column chart by `fare_bin`  
- Highlights fares in range `$2.50–$10.00`

### Fare vs. Distance 📍  
- Scatter plot of `fare_amount` vs. `distance_miles`  
- Bubble size = ride count  
- Shows strong correlation

### Fare by Hour ⏰  
- Line chart of average fare by hour  
- Peaks around `$12` during 7–9 AM and 4–6 PM  

### Geographic Distribution 🌍  
- Map using `pickup_latitude` and `pickup_longitude`  
- High density in Manhattan  

### Busiest Periods 📅  
- Bar chart of ride counts by hour  
- Highlight peak hours (7–9 AM, 4–6 PM)

### Slicers 🔎  
- Filters for `day_of_week`, `month`, `is_peak_hour`  
- Enables dynamic exploration of trends

---

## 🚀 **Instructions to Run the Project**

### 1. _Clone the Repository_
```bash
git clone https://github.com/amazezerti/Uber-Fares-PowerBI-Project.git


### 2. _Set Up Python Environment_ 🐍  
- [Download Anaconda](https://www.anaconda.com/products/distribution)  
- Install required libraries:
```bash
pip install pandas numpy geopy matplotlib seaborn
```

### 3. _Run Preprocessing_  
- Open `uber_data_preprocessing.py` in Jupyter Notebook  
- Ensure `uber.csv` is in the same folder  
- Run to generate `uber_fares_cleaned.csv`

### 4. _Run EDA_  
- Open `uber_eda.py`  
- Ensure `uber_fares_cleaned.csv` is available  
- Run to generate `.png` plots in `/screenshots`

### 5. _View Dashboard_ 🖼
- [Download Power BI Desktop](https://powerbi.microsoft.com/desktop/)  
- Open `uber_fares_dashboard.pbix`  
- Or re-import the CSV and recreate visuals manually

---

## 📊 **Key Findings**

- **Average fare** ≈ `$10.50`, peaks at `$12` during rush hours  
- **Distance correlation:** `r ≈ 0.70` between fare and miles  
- **Fridays and Saturdays:** ~30% of rides  
- **Peak hours:** ~25% of activity  
- **Manhattan:** Highest ride density

---

## 💡 **Recommendations**

- 🚖 Deploy more drivers during peak hours and weekends  
- 💸 Implement surge pricing for trips over 5 miles  
- 🗺 Focus driver availability in Manhattan  
- 📣 Promote group rides for passengers (5–6)

---

## 📸 **Screenshots Folder**

- `data_import.png` – Power BI Data View  
- `power_query.png` – Power Query Editor  
- `dashboard.png` – Final dashboard  
- `fare_distribution.png` – Histogram  
- `fare_vs_distance.png` – Scatter plot  
- `fare_by_hour.png` – Line chart

---

## 🙏 **Acknowledgments**

- Kaggle – For the dataset  
- Lecturer Eric Maniraguha – For guidance  
- Power BI Community – For dashboard resources


