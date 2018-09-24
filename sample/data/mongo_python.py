import pymongo
from bson.objectid import ObjectId

MONGO_URI= 'ds115971.mlab.com'
PORT = 15971
DB_NAME = 'moocrec'
USER = 'bitplease10'
PASS = 'bitplease10'
    
def insert_topics(topics):
    
    
    #Connect with the mlab mongo database
    connection = pymongo.MongoClient(MONGO_URI,PORT)
    db = connection[DB_NAME]
    db.authenticate(USER, PASS)
    
    #insert data into mooocs_course_topic
    collection = db.moocs_course_topics 
    result = collection.insert_one(topics)
    return format(result.inserted_id)

    
    #5b317f2b54b99d19f00fed50
    
def update_record_byId(course_id, topics):
    
    #Connect with the mlab mongo database
    connection = pymongo.MongoClient(MONGO_URI,PORT)
    db = connection[DB_NAME]
    db.authenticate(USER, PASS)
    
    #update data into mooocs_course
    collection = db.moocs_course
    
    _id = { "_id" : ObjectId(course_id) }
    _values = { "$set": topics }
    
    result = collection.find_and_modify(_id,_values)
    return result


def update_record_byName(course_name, topics):
    
    #Connect with the mlab mongo database
    connection = pymongo.MongoClient(MONGO_URI,PORT)
    db = connection[DB_NAME]
    db.authenticate(USER, PASS)
    
    #update data into mooocs_course
    collection = db.moocs_course
    
    _id = { "course_name" : course_name }
    _values = { "$set": topics }
    
    result = collection.find_and_modify(_id,_values)
    return result





