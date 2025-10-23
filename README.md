🛍️ Sales Data Analysis with MySQL & Python

📌 Overview
This project connects to a MySQL database, retrieves sales data, and performs data analysis and visualization using Python libraries such as Pandas, NumPy, Matplotlib, and Seaborn.
It provides insights into sales performance over time, across products, and across regions.

⚙️ Workflow
🔹 1. Database Connection
    • Establishes a secure connection to a local MySQL database.
    • Verifies the connection before executing any operations.
🔹 2. Data Extraction
    • Executes a SQL query (SELECT * FROM sales) to fetch all records from the sales table.
    • Loads the retrieved data into a Pandas DataFrame for analysis.
🔹 3. Data Preprocessing
    • Converts the order_date column into datetime format for proper time-based analysis.
    • Creates a new column total_sales by multiplying quantity × price to calculate revenue per order.

📊 Analysis & Visualizations
📈 a. Daily Sales Trend
    • Groups data by order_date and sums up daily sales.
    • Visualizes overall sales trends using a line chart to identify growth patterns and fluctuations.
🧾 b. Product-wise Sales
    • Aggregates total sales by each product.
    • Displays the results using a bar chart, highlighting top-performing products.
🌍 c. Regional Sales Performance
    • Groups data by region and calculates total sales.
    • Uses a bar chart to compare sales performance across different regions.
🔍 d. Correlation Analysis
    • Examines the relationship between quantity, price, and total_sales.
    • Presents the correlation using a heatmap to visualize how strongly these variables are related.

🧩 Libraries Used
mysql.connector – to connect and query the MySQL database.
pandas – for data manipulation and analysis.
numpy – for numerical computations.
matplotlib.pyplot – for creating visual charts.
seaborn – for advanced and aesthetic statistical plots.

🎯 Key Insights
✅ Identify sales trends over time.
✅ Discover best-selling products.
✅ Compare performance across regions.
✅ Analyze relationships between price, quantity, and total revenue.
