from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    json_path = os.path.join(app.root_path, 'items.json')

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        # If reading/parsing fails, pass an empty list
        print(f"Error loading items.json: {e}")
        items_list = []
    else:
        # Safely extract the "items" key (might be missing)
        items_list = data.get('items', [])
        # Ensure it's actually a list
        if not isinstance(items_list, list):
            items_list = []

    # 3. Render the template, passing the list
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
