from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

def read_json_data():
    path = os.path.join(app.root_path, 'products.json')
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []

def read_csv_data():
    path = os.path.join(app.root_path, 'products.csv')
    products = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert id and price to proper types
                try:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                except ValueError:
                    continue
                products.append(row)
    except Exception:
        pass
    return products

@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    id_arg = request.args.get('id')
    error = None

    # 1. Load data from the chosen source
    if source == 'json':
        data = read_json_data()
    elif source == 'csv':
        data = read_csv_data()
    else:
        data = []
        error = 'Wrong source: must be "json" or "csv".'

    # 2. If an id filter was given, apply it
    products_list = data
    if not error and id_arg:
        try:
            target_id = int(id_arg)
        except ValueError:
            products_list = []
            error = 'Invalid id parameter.'
        else:
            filtered = [p for p in data if p.get('id') == target_id]
            if filtered:
                products_list = filtered
            else:
                products_list = []
                error = 'Product not found.'

    # 3. Render the template
    return render_template(
        'product_display.html',
        products=products_list,
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
