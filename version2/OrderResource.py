from flask import Flask
from flask import request
from flask import jsonify
from Order import Order, posts, delete_order_db
from OrderItem import OrderItem
from bson.json_util import dumps


app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({
        'author': 'Gaurav Misra',
        'application': 'Starbucks V3 implementation'
    })


@app.route('/starbucks/order', methods=['POST'])
def neworder():
    x = request.get_json(force=True)
    if request.method == 'POST':
        order = Order(x['location'])
        items = x['items']
        for i in items:
            qty = i['qty']
            name = i['name']
            milk = i['milk']
            size = i['size']
            orderitem = OrderItem(qty, name, milk, size)
            order.items.append(orderitem)
        order.status = 'PLACED'
        order.message = 'Order has been placed'
        order.add_order_db()
        resp = jsonify(posts.find_one({'id': order.id}, {'_id': False}))
        resp.status_code = 201
        return resp


@app.route('/starbucks/order/<string:order_num>', methods=['DELETE'])
def del_order(order_num):
    if request.method == 'DELETE':
        delete_order_db(order_num)
        resp = jsonify({})
        resp.status_code = 204
        return resp


@app.route('/starbucks/order/<string:order_num>', methods=['GET'])
def get_order(order_num):
    if request.method == 'GET':
        resp = jsonify(posts.find_one({'id': order_num}, {'_id': False}))
        resp.status_code = 200
        return resp


@app.route('/starbucks/order/<string:order_num>', methods=['PUT'])
def update_order(order_num):
    x = request.get_json(force=True)
    if request.method == 'PUT':
        o_status = (posts.find_one({'id': order_num}, {'_id': 0, 'id': 0, 'location': 0, 'items': 0, 'message': 0,
                    'links': 0}))
        print "current order status retrieved from db is" + o_status['status']
        if o_status['status'] != 'PLACED':
            return jsonify({'status': 'Order is getting prepared, cannot update!!'})
        else:
            get_updated = posts.update_one({'id': order_num},
                                           {'$set': {'location': x['location'],
                                            'items': x['items'],
                                            'status': 'REPLACED',
                                            'message': 'Order has been replaced'}})
            print get_updated.modified_count
            resp = jsonify(posts.find_one({'id': order_num}, {'_id': False}))
        resp.status_code = 202
        return resp


@app.route('/starbucks/orders', methods=['GET'])
def get_all_orders():
    orders = posts.find(projection={'_id': False})
    return dumps(orders)


@app.route('/starbucks/order/<string:order_num>/pay', methods=['POST'])
def pay_order(order_num):
    posts.update_one({'id': order_num},
                     {'$set': {'message': 'Payment done, preparing...', 'status': 'PAID'}})
    resp = jsonify(posts.find_one({'id': order_num}, {'_id': False}))
    resp.status_code = 201
    print "order has been paid for"
    return resp

# running the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
