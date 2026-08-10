import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/items')
def items():
    # Read items from the JSON file
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []

    # Render template with items list
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
