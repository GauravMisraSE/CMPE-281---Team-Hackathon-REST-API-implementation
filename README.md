# CMPE-281-Team-Hackathon-REST-API-implementation

### Tech stack:
### DB: Mongo
### APIs: Pyhton flask

### AWS config:
#### Starbucks API node: holds the API endpoints for placing, paying, updating, viewing and deleting orders.
#### Mongo Primary: Receives write and read requests
#### Mongo Slaves: Can only be used for reading. Data written to Primary is replicated to slaves.

### Class description:
OrderItem: class for taking quantity, name, milk and size.  
Order: for generating payload which is saved as a document, this class also contains method to delete order from db.  
OrderResource: contains API routes.  
Status: for modelling order status and message.  
sweeper.py: Runs continuously in the background and updates order statuses after every 60 seconds. 

### Youtube Demonstration link:  
https://www.youtube.com/watch?v=bH9-TJym5Ek

