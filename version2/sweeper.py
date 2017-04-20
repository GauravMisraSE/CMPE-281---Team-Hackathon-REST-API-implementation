from Order import posts
import time

while True:
    update_paid = posts.update_many({'status': 'PAID'}, {'$set': {'status': 'PREPARING'}})
    time.sleep(20)
    update_preparing = posts.update_many({'status': 'PREPARING'}, {'$set': {'status': 'SERVED'}})
    time.sleep(20)
    update_served = posts.update_many({'status': 'SERVED'}, {'$set': {'status': 'COLLECTED'}})
    time.sleep(20)
    print "number of orders preparing = " , update_paid.modified_count
    print "number of orders served = " , update_preparing.modified_count
    print "number of orders collected = " , update_served.modified_count
