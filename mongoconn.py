from pymongo import MongoClient

client =MongoClient('localhost', 27017)
db = client['orderdb']
collection = db['orders']
posts =db.posts
msg = {
    'hello':'hello1'
}
postmsg = posts.insert_one(msg)
print "db created"



