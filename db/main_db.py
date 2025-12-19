import sqlite3
from db import queries
from config import path_db

def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_PRODUCT)
    print("База данных подключена")
    conn.commit()
    conn.close()


def add_product(product):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.INSERT_PRODUCTS, (product, ))
    conn.commit()
    product_id = cursor.lastrowid
    conn.close()
    return product_id


def get_products(filter_type): 
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    if filter_type == 'completed':
        cursor.execute(queries.SELECT_PRODUCTS_COMPLETED)
    elif filter_type == 'uncompleted':
        cursor.execute(queries.SELECT_PRODUCTS_UNCOMPLETED)
    else:
        cursor.execute(queries.SELECT_PRODUCTS)

    products = cursor.fetchall()
    conn.close()
    return products

def get_len_products():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.SELECT_COUNT_COMPLETED_PRODUCTS)
    count = cursor.fetchone()[0]
    return count


def update_products(product_id, new_product=None, completed=None):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    
    if new_product is not None:
        cursor.execute(queries.UPDATE_PRODUCTS, (new_product, product_id))
        
    if completed is not None:
        cursor.execute("UPDATE products SET completed = ? WHERE id = ?", (completed, product_id))

    conn.commit()
    conn.close()


def delete_products(product_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_PRODUCTS, (product_id,))
    conn.commit()
    conn.close()

def del_completed_product():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_COMPLETED_PRODUCT)
    conn.commit()
    conn.close()