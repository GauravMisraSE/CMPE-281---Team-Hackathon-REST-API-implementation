import uuid
from pymongo import MongoClient
#from urlparse import urlparse

client = MongoClient('ec2-54-193-71-217.us-west-1.compute.amazonaws.com', 27017)
db = client['orderdb']
collection = db['orders']
posts = db.posts


class Order(object):

    def __init__(self, loc):
        self.id = str(uuid.uuid1())
        print (self.id)
        self.location = loc
        self.items = []
        self.links = {}
        self.status = "status not defined"
        self.message = "message not available"

    def add_order_db(self):
        itemarray =[]
        item_map ={}
        for i in self.items:
            item_map['qty'] = i.qty
            item_map['name'] = i.name
            item_map['milk'] = i.milk
            item_map['size'] = i.size
            itemarray.append(item_map)
        self.links['payment'] = "http://0.0.0.0:5000/starbucks/order/"+self.id+"/pay"
        self.links['order'] = "http://0.0.0.0:5000/starbucks/order/" + self.id
        #print itemarray
        msg = {
            'id': self.id,
            'location': self.location,
            'items': itemarray,
            'links': self.links,
            'status': self.status,
            'message': self.message
        }
        insert_db = posts.insert_one(msg).inserted_id
        print insert_db
        return


def delete_order_db(order_id):
    resource = {
        'id': order_id
    }
    result = posts.delete_one(resource)
    print(result.deleted_count)
    return





