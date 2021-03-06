import sqlite3

def query(query_text, *param):
    conn = sqlite3.connect('Northwind_small.sqlite')
    cur = conn.cursor()
    cur.execute(query_text, param)

    column_names= []
    for column in cur.description:
        column_names.append(column[0])

    rows = cur.fetchall()
    dicts = []

    for row in rows:
        d = dict(zip(column_names,row))
        dicts.append(d)

    conn.close()
    return dicts

def get_all_suppliers():
    return query("""SELECT * FROM Supplier ORDER BY CompanyName""")


def get_supplier_products(supplier_id):
    return query("""SELECT * FROM Product
    WHERE SupplierId = ?""", supplier_id)

def get_company(supplier_id):
    return query("""SELECT CompanyName FROM Supplier
    WHERE Id = ?""", supplier_id)

def get_all_categories():
    return query("""
        SELECT CategoryId, Category.CategoryName, Category.Description, COUNT(Product.Id) AS ProductCount 
        FROM Product
        INNER JOIN Category
            ON Product.CategoryId = Category.Id 
        GROUP BY CategoryName
        """)

def get_categories_by_id(category_id):
    return query("""
        SELECT SupplierId, ProductName, CompanyName, CategoryName 
        FROM Product
        INNER JOIN Supplier
            ON Product.SupplierId = Supplier.Id
        INNER JOIN Category
            ON Product.CategoryId = Category.Id
            WHERE CategoryId = ?
    """, category_id)
