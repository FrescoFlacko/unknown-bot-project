from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

def initializeMongoDBService():
    '''
        Initializes the MongoDB client for the project and
        sets a global database object to be used in project.
    '''
    mongo_client = MongoClient('mongodb://127.0.0.1:27017/', serverSelectionTimeoutMS=1000)

    try :
        mongo_client.admin.command('ismaster')
    except ServerSelectionTimeoutError as error:
        print('ERROR while trying to initialize MongoDB:', error)
        return False
    
    global trades_db 
    trades_db = mongo_client['trades']

    return True

def retrieveAllFromCollection(collection):
    '''
        Retrieves all the documents from a given collection.
    '''
    mongo_collection = getCollectionObject(collection)
    if (mongo_collection == None):
        return
    
    response = mongo_collection.find()
    return response

def insertDocument(collection, document):
    '''
        Insert a document into the collection.
    '''
    mongo_collection = getCollectionObject(collection)
    if (mongo_collection == None):
        return
    
    # Remove _id field when inserting document so we can use Mongo-generated ID
    document_dict = document.__dict__
    del document_dict['_id']
    
    response = mongo_collection.insert_one(document_dict)
    document._id = response.inserted_id

    return response

def updateDocument(collection, document):
    '''
        Update the document in the given collection.
    '''
    mongo_collection = getCollectionObject(collection)
    if (mongo_collection == None):
        return
    
    query = { "_id" : document._id }

    response = mongo_collection.update_one(query, document.__dict__)
    return response

def removeDocument(collection, document):
    '''
        Remove the given document from the collection.
    '''
    mongo_collection = getCollectionObject(collection)
    if (mongo_collection == None):
        return
    
    query = { "_id" : document._id }

    response = mongo_collection.insert_one(document.__dict__)
    return response

def getCollectionObject(collection):
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