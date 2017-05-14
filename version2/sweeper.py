from Order import posts
import time
while True:
        time.sleep(60)
    	update_paid = posts.update_many({'status': 'PAID'}, {'$set': {'status': 'PREPARING','message':'Order is being prepared'}})
        time.sleep(60)
    	update_preparing = posts.update_many({'status': 'PREPARING'}, {'$set': {'status': 'SERVED','message':'Order served'}})
        time.sleep(60)	
    	update_served = posts.update_many({'status': 'SERVED'}, {'$set': {'status': 'COLLECTED','message':'Order collected, Thankyou!!'}})	
   # print "number of orders preparing = " , update_paid.modified_count
   # print "number of orders served = " , update_preparing.modified_count
   # print "number of orders collected = " , update_served.modified_count
