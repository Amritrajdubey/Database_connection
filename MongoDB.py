import pymongo # Importing Mongodb

client = pymongo.MongoClient("mongodb+srv://Raj222:<password>@mongoproject.5m6hl7p.mongodb.net/?retryWrites=true&w=majority")
# Setting up connections
db = client.test
print(db)

