import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

# One-to-One Join
employees_offices = pd.read_sql("""
                                SELECT firstName, lastName, city, state
                                FROM employees
                                JOIN offices
                                USING(officeCode)
                                ORDER BY firstName, lastName;
                                """, conn)

# print(employees_offices)

# One-to-Many Join
customers_orders = pd.read_sql("""
                               SELECT customerNumber, contactFirstName, contactLastName, orderNumber, orderDate, status
                               FROM customers
                               JOIN orders
                               USING(customerNumber)
                               ORDER BY customerNumber;
                               """, conn)

# print(customers_orders)

# One-to-Many Join
customers_payments = pd.read_sql("""
                                 SELECT customerNumber, contactFirstName, contactLastName, checkNumber, paymentDate, amount
                                 FROM customers
                                 JOIN payments
                                 USING(customerNumber)
                                 ORDER BY amount DESC;
                                 """, conn)

# print(customers_payments)

# Many-to-Many Join
order_details_product_details = pd.read_sql("""
                                            SELECT customerNumber, contactFirstName, contactLastName, productCode, productName, quantityOrdered, orderDate
                                            FROM customers
                                            JOIN orders
                                              USING(customerNumber)
                                            JOIN orderDetails
                                              USING(orderNumber)
                                            JOIN products
                                              USING(productCode)
                                            ORDER BY orderDate DESC;
                                            """, conn)

print(order_details_product_details)

conn.close()