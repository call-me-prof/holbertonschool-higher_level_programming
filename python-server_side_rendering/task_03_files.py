import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json_file(filepath):
    """Read and parse product data from a JSON file."""
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except Exception:
        return []

def read_csv_file(filepath):
    """Read and parse product data from a CSV file."""
    products = []
    try:
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
    except Exception:
        pass
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Validate source parameter
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # Load data from the specified source
    if source == 'json':
        products = read_json_file('products.json')
    else:
        products = read_csv_file('products.csv')

    # Filter by product_id if provided
    if product_id:
        try:
            target_id = int(product_id)
            products = [p for p in products if p.get('id') == target_id]
            if not products:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
