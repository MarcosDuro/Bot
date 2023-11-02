import pymongo


MONGO_URI = 'mongodb://localhost'
client = pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=5000)
database = client['users']
collection = database['usuarios']
collection_dos = database['keys']
collection_tres = database['groups']
