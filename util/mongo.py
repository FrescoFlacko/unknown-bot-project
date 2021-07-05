import pymongo

def initializeMongoDBService():
    '''
        Initializes the MongoDB client for the project and
        sets a global database object to be used in project.
    '''
    mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
    global trades_db 
    trades_db = mongo_client['trades']

def retrieveAllFromCollection(collection):
    '''
        Retrieves all the documents from a given collection.
    '''
    mongo_collection = getCollectionObject()
    if (mongo_collection == None):
        return
    
    response = mongo_collection.find()
    return response

def insertDocument(collection, document):
    '''
        Insert a document into the collection.
    '''
    mongo_collection = getCollectionObject()
    if (mongo_collection == None):
        return
    
    response = mongo_collection.insert_one(document)
    return response

def updateDocument(collection, document):
    '''
        Update the document in the given collection.
    '''
    mongo_collection = getCollectionObject()
    if (mongo_collection == None):
        return
    
    query = { "_id" : document._id }

    response = mongo_collection.update_one(query, document)
    return response

def removeDocument(collection, document):
    '''
        Remove the given document from the collection.
    '''
    mongo_collection = getCollectionObject()
    if (mongo_collection == None):
        return
    
    query = { "_id" : document._id }

    response = mongo_collection.insert_one(document)
    return response

def getCollectionObject(collection_name):
    '''
        Create the collection pymongo object to be used when making
        CRUD instructions.
    '''
    if (trades_db == None):
        print('ERROR: Mongo service has not been initialized.')
        return
    
    mongo_collection = trades_db[collection]
    if (mongo_collection == None):
        print("ERROR: Collection does not exist in Mongo database.")
        return
    
    return mongo_collection