-- 1. Top 5 Products by Revenue
SELECT product_name, SUM(sales) AS total_sales
FROM superstore
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 5;

-- 2. Monthly Sales Trend
SELECT strftime('%Y-%m', order_date) AS month,
SUM(sales) AS total_sales
FROM superstore
GROUP BY month
ORDER BY month;

-- 3. Sales by Category
SELECT category, SUM(sales) AS total_sales
FROM superstore
GROUP BY category
ORDER BY total_sales DESC;

-- 4. Top 5 Cities by Sales
SELECT city, SUM(sales) AS total_sales
FROM superstore
GROUP BY city
ORDER BY total_sales DESC
LIMIT 5;

-- 5. Average Order Value
SELECT AVG(sales) AS avg_order_value
FROM superstore;

-- 6. Total Profit by Category
SELECT category, SUM(profit) AS total_profit
FROM superstore
GROUP BY category
ORDER BY total_profit DESC;

-- 7. Products with Highest Quantity Sold
SELECT product_name, SUM(quantity) AS total_quantity
FROM superstore
GROUP BY product_name
ORDER BY total_quantity DESC
LIMIT 5;

-- 8. Sales in 2024
SELECT SUM(sales) AS total_sales_2024
FROM superstore
WHERE order_date BETWEEN '2024-01-01' AND '2024-12-31';

-- 9. Sales by City and Category
SELECT city, category, SUM(sales) AS total_sales
FROM superstore
GROUP BY city, category
ORDER BY total_sales DESC;

-- 10. Highest Profit Products
SELECT product_name, SUM(profit) AS total_profit
FROM superstore
GROUP BY product_name
ORDER BY total_profit DESC
LIMIT 5;

-- 11. Orders Count by Category
SELECT category, COUNT(order_id) AS total_orders
FROM superstore
GROUP BY category
ORDER BY total_orders DESC;

-- 12. Revenue Per City
SELECT city, SUM(sales) AS total_revenue
FROM superstore
GROUP BY city
ORDER BY total_revenue DESC;
