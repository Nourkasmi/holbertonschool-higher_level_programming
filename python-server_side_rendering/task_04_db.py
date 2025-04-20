from flask import Flask, render_template, request
import json, csv, os, sqlite3

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
                try:
                    row['id']       = int(row['id'])
                    row['price']    = float(row['price'])
                except ValueError:
                    continue
                products.append(row)
    except Exception:
        pass
    return products

def read_sql_data():
    db_path = os.path.join(app.root_path, 'products.db')
    products = []
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for id_, name, category, price in rows:
            products.append({
                'id':       id_,
                'name':     name,
                'category': category,
                'price':    price
            })
    except Exception as e:
        print(f"DB error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
    return products

@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    id_arg = request.args.get('id')
    error = None

    # 1. Choose data source
    if source == 'json':
        data = read_json_data()
    elif source == 'csv':
        data = read_csv_data()
    elif source == 'sql':
        data = read_sql_data()
    else:
        data = []
        error = 'Wrong source: must be "json", "csv", or "sql".'

    # 2. Filter by id if requested
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

    # 3. Render same template as before
    return render_template(
        'product_display.html',
        products=products_list,
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
