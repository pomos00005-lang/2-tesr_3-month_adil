CREATE_PRODUCT ="""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    )
"""

INSERT_PRODUCTS = 'INSERT INTO products (product) VALUES (?)'

SELECT_PRODUCTS = "SELECT id,product,completed FROM products"

SELECT_PRODUCTS_UNCOMPLETED = "SELECT id,product,completed FROM products WHERE completed = 0"

SELECT_PRODUCTS_COMPLETED = "SELECT id,product,completed FROM products WHERE completed = 1"

SELECT_COUNT_COMPLETED_PRODUCTS = 'SELECT COUNT (*) FROM products WHERE completed = 1'


UPDATE_PRODUCTS = "UPDATE products SET product = ? WHERE id = ?"

DELETE_PRODUCTS = 'DELETE FROM products WHERE id = ?'

DELETE_COMPLETED_PRODUCT = 'DELETE FROM products WHERE completed = 1'

