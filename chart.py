import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="s"
)

if conn.is_connected():
    print("Connected to mysql database")

query = "SELECT * FROM sales"
df = pd.read_sql_query(query, conn)

df['order_date'] = pd.to_datetime(df['order_date'])

df['total_sales'] = df['quantity'] * df['price']

######
daily_sales = df.groupby('order_date')['total_sales'].sum().reset_index()

plt.figure(figsize=(4, 4))
plt.plot(daily_sales['order_date'], daily_sales['total_sales'])
plt.title('Sales Trend')
plt.xlabel('Order Date')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

#####
product_sales = df.groupby('product')['total_sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(4,4))
product_sales.plot(kind='bar', color='black')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

####
region_sales = df.groupby('region')['total_sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(4,4))
region_sales.plot(kind='bar', color='blue')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#####
corr_matrix = df[['quantity', 'price', 'total_sales']].corr()

plt.figure(figsize=(4,4))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Between Quantity, Price, and Total Sales')
plt.tight_layout()
plt.show()

