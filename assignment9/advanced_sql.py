import sqlite3

DB_PATH = "/Users/jhojanfvp/python_homework/python_homework/db/lesson.db"


# Task 1: Complex JOINs with Aggregation

print("Task 1: Total price of first 5 orders")
with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()
    query = """
    SELECT o.order_id,
           SUM(p.price * l.quantity) AS total_price
    FROM orders AS o
    JOIN line_items AS l ON o.order_id = l.order_id
    JOIN products AS p ON l.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
    LIMIT 5;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    print(results, "\n")


# Task 2: Understanding Subqueries

print("Task 2: Average price of each customer's orders")
with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()
    query = """
    SELECT c.customer_name, AVG(totalOrders.total_price) AS average_total_price
    FROM customers AS c
    LEFT JOIN (
        SELECT o.customer_id AS customer_id_b, SUM(l.quantity * p.price) AS total_price
        FROM orders AS o 
        JOIN line_items AS l ON o.order_id = l.order_id 
        JOIN products AS p ON l.product_id = p.product_id
        GROUP BY o.order_id
    ) AS totalOrders ON c.customer_id = totalOrders.customer_id_b
    GROUP BY c.customer_id
    ORDER BY c.customer_name;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    print(results, "\n")


# Task 3: Insert Transaction (idempotent)

print("Task 3: Create new order for 'Perez and Sons'")
with sqlite3.connect(DB_PATH) as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()
    try:
        # Get IDs
        cursor.execute("SELECT customer_id FROM customers WHERE customer_name = ?", ('Perez and Sons',))
        customer_id = cursor.fetchone()[0]

        cursor.execute("SELECT employee_id FROM employees WHERE first_name=? AND last_name=?", ('Miranda', 'Harris'))
        employee_id = cursor.fetchone()[0]

        cursor.execute("SELECT product_id FROM products ORDER BY price LIMIT 5")
        product_ids = [row[0] for row in cursor.fetchall()]

        # Check if an order already exists for this customer today
        cursor.execute("""
            SELECT order_id FROM orders
            WHERE customer_id = ? AND employee_id = ? AND date = DATE('now')
        """, (customer_id, employee_id))
        row = cursor.fetchone()

        if row:
            order_id = row[0]  # reuse existing order
        else:
            # Insert new order
            cursor.execute(
                "INSERT INTO orders (customer_id, employee_id, date) VALUES (?, ?, DATE('now'))",
                (customer_id, employee_id)
            )
            order_id = cursor.lastrowid

        # Insert line_items (only if not already there)
        for product_id in product_ids:
            cursor.execute("""
                INSERT OR IGNORE INTO line_items (order_id, product_id, quantity)
                VALUES (?, ?, ?)
            """, (order_id, product_id, 10))

        conn.commit()
    except Exception as e:
        conn.rollback()
        print("Error:", e)

    # Verify insertion
    query = """
    SELECT l.line_item_id, p.product_name, l.quantity
    FROM line_items AS l
    JOIN products AS p ON l.product_id = p.product_id
    WHERE l.order_id = ?
    """
    cursor.execute(query, (order_id,))
    result = cursor.fetchall()
    print(result, "\n")



# Task 4: Aggregation with HAVING

print("Task 4: Employees with more than 5 orders")
with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()
    query = """
    SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
    FROM employees AS e
    JOIN orders AS o ON e.employee_id = o.employee_id
    GROUP BY e.employee_id
    HAVING COUNT(o.order_id) > 5;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
