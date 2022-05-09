from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route("/")
def suppliers():
    suppliers = database.get_all_suppliers()
    return render_template('index.html', suppliers=suppliers)

@app.route("/suppliers/<int:supplier_id>")
def products(supplier_id):
    products = database.get_supplier_products(supplier_id)
    suppliers = database.get_company(supplier_id)
    return render_template('products.html', products=products, suppliers=suppliers)

@app.route("/categories")
def food_categories():
    food_categories = database.get_all_categories()
    return render_template('category.html', food_categoties=food_categories)