# 🍔 Food Delivery & Cloud Kitchen Market Analysis (Bengaluru)

## 📌 Executive Summary
This project analyzes a massive food delivery dataset (based on Zomato Bangalore data) to uncover actionable business insights for cloud kitchens and restaurant aggregators. By examining over 50,000 restaurant records, this analysis identifies prime locations for new cloud kitchens, correlates late-night delivery availability with customer retention, and maps the most profitable cuisines by neighborhood.

## 🛠 Tech Stack
- **Data Manipulation & Cleaning:** Python (Pandas, NumPy)
- **Database & Querying:** PostgreSQL
- **Data Visualization:** Tableau / Power BI 

## ⚙️ Methodology
1. **Data Wrangling:** Cleaned raw text strings, imputed missing numerical values (like costs and ratings), and standardized categorical data (cuisines, locations).
2. **Exploratory Data Analysis (SQL):** Aggregated data using window functions and CTEs to rank neighborhoods and evaluate pricing tiers.
3. **Visualization:** Built interactive dashboards to geographically map restaurant density versus average order value.

## 💡 Key Business Insights
1. **The "Late-Night Dessert" Premium:** Restaurants in K.R. Puram offering late-night dessert options maintain a 15% higher average rating and order volume.
2. **Untapped Cloud Kitchen Zones:** Certain layouts have high demand for North Indian cuisine but a low density of high-rated cloud kitchens, making them prime expansion targets.
3. **Price Elasticity in Fast Food:** Items like chicken burgers and popcorn chicken see a massive drop in order volume when priced above ₹350 for two, indicating high price sensitivity.

## 🚀 How to Run the Code
1. Clone the repository: `git clone https://github.com/yourusername/food-delivery-market-analysis.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the cleaning script: `python scripts/01_data_cleaning.py`
4. Execute the SQL queries in your preferred database IDE.
