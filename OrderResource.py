from flask import Flask
from flask import request
from flask import jsonify
from Order import Order, posts
from OrderItem import OrderItem

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
# Creating response
#        resp = jsonify({
#            'id': order.id,
#            'location': order.location,
#            #'items': order.items,
#            'links': order.links,
#            'status': order.status,
#            'message': order.message
#        })
        resp = jsonify(posts.find_one({'id':order.id}, {'_id': False}))
        resp.status_code = 201
        return resp

# running the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
