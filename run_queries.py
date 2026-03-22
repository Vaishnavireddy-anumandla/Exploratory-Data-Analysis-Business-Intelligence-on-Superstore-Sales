import sqlite3
import pandas as pd
import os

# Make sure outputs folder exists
os.makedirs("query_results", exist_ok=True)

# Connect to SQLite database
conn = sqlite3.connect("superstore.db")

# Dictionary of queries
queries = {
    "top_5_products_by_revenue": """
        SELECT product_name, SUM(sales) AS total_sales
        FROM superstore
        GROUP BY product_name
        ORDER BY total_sales DESC
        LIMIT 5;
    """,

    "monthly_sales_trend": """
        SELECT strftime('%Y-%m', order_date) AS month,
        SUM(sales) AS total_sales
        FROM superstore
        GROUP BY month
        ORDER BY month;
    """,

    "sales_by_category": """
        SELECT category, SUM(sales) AS total_sales
        FROM superstore
        GROUP BY category
        ORDER BY total_sales DESC;
    """,

    "top_5_cities_by_sales": """
        SELECT city, SUM(sales) AS total_sales
        FROM superstore
        GROUP BY city
        ORDER BY total_sales DESC
        LIMIT 5;
    """,

    "average_order_value": """
        SELECT AVG(sales) AS avg_order_value
        FROM superstore;
    """,

    "total_profit_by_category": """
        SELECT category, SUM(profit) AS total_profit
        FROM superstore
        GROUP BY category
        ORDER BY total_profit DESC;
    """,

    "highest_quantity_products": """
        SELECT product_name, SUM(quantity) AS total_quantity
        FROM superstore
        GROUP BY product_name
        ORDER BY total_quantity DESC
        LIMIT 5;
    """,

    "sales_in_2024": """
        SELECT SUM(sales) AS total_sales_2024
        FROM superstore
        WHERE order_date BETWEEN '2024-01-01' AND '2024-12-31';
    """,

    "sales_by_city_and_category": """
        SELECT city, category, SUM(sales) AS total_sales
        FROM superstore
        GROUP BY city, category
        ORDER BY total_sales DESC;
    """,

    "highest_profit_products": """
        SELECT product_name, SUM(profit) AS total_profit
        FROM superstore
        GROUP BY product_name
        ORDER BY total_profit DESC
        LIMIT 5;
    """,

    "orders_count_by_category": """
        SELECT category, COUNT(order_id) AS total_orders
        FROM superstore
        GROUP BY category
        ORDER BY total_orders DESC;
    """,

    "revenue_per_city": """
        SELECT city, SUM(sales) AS total_revenue
        FROM superstore
        GROUP BY city
        ORDER BY total_revenue DESC;
    """
}

# Execute all queries and save results
for name, query in queries.items():
    df = pd.read_sql(query, conn)
    file_path = f"query_results/{name}.csv"
    df.to_csv(file_path, index=False)
    print(f"Saved output of {name} to {file_path}")

# Close connection
conn.close()
