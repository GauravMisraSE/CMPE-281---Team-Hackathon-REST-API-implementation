import uuid
from pymongo import MongoClient

client =MongoClient('localhost', 27017)
db = client['orderdb']
collection = db['orders']
posts = db.posts

class Order(object):

    def __init__(self, loc):
        self.id = uuid.uuid1()
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
            item_map['qty']=i.qty
            item_map['name']=i.name
            item_map['milk']=i.milk
            item_map['size']=i.size
            itemarray.append(item_map)
        print itemarray
        msg = {
            'id' :self.id,
            'location':self.location,
            'items':itemarray,
            'links':self.links,
            'status':self.status,
            'message':self.message
        }
        insertdb = posts.insert_one(msg).inserted_id
        print insertdb





