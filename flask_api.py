# It should be known that this is not a true RESTful API
from flask import Flask, jsonify, request
from flask import render_template

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
            'name': 'My Item',
            'price': 15.99
            }
        ]
    }
]

# This template is here so that users can call my api from a browser
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json() # this is how the requests module
    new_store = {                     # accepts input for POST
        'name': request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})
# jsonify is what makes this a web API

@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
                }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'item not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_store_item(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store item not found'})

@app.route('/store', methods=['DELETE'])
def del_store(name):
    store_del = request.delete()
    for store in stores:
        if store['name'] == name:
            stores.remove(store_del[0])
        return jsonify({'stores': stores})

# the app is actually running on port 5000
app.run(port=None)
