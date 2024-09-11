import datetime
import os
import certifi
from dotenv import load_dotenv
from pymongo import MongoClient
from pprint import pprint
import bson
load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

#connect to MongoDB cluster
client = MongoClient(MONGODB_URI,tlsCAFile=certifi.where())

#list all the databases in the cluster:
for db_info in client.list_database_names():
    print(db_info)

#get a reference to the sample_mflix database
db = client['sample_mflix']

#list all the connections in 'sample_mflix'
collections = db.list_collection_names()
for collection in collections:
    print(collection)


print("========================================\n")
#get a reference to the movies collection
movies = db['movies']
# docs = movies.find()
# for d in docs:
#     pprint(d)
print("\n==============")
pprint(movies.find_one({'title':'Bhoothnath Returns'}))

'''inserting parasite'''
insert_result = movies.insert_one({
    "title":"Parasite",
    "year":2020,
    "plot":"A poor family, the Kims, con their way into becoming the servants of a rich family, the parks"
    "But their easy life gets complicated when their deception is threatended with exposure",
    "released": datetime.datetime(2020,2,7,0,0,0),
})

#save the inserted_id of the document you just created:
parasite_id = insert_result.inserted_id
print("_id of insterted document:{parasite_id}".format(parasite_id=parasite_id))
print(movies.find_one({'_id':bson.ObjectId(parasite_id)}))


#looking up the documents that you've created in the collection:
cnt = 0
for doc in movies.find({"title":"Parasite"}):
    cnt+=1
    pprint(doc)
print("I've inserted the document",cnt,"times")

#update the documents wit the correct year:
update_result = movies.update_one({'_id': parasite_id},{
    '$set':{"year":2019}
})

#print out the updated record to make sure it's correct
pprint(movies.find_one({'_id':parasite_id}))
