import datetime
import os
import certifi
from dotenv import load_dotenv
from pymongo import MongoClient
from pprint import pprint
import bson
print('...from moreMongoDb')
# load_dotenv
load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']
#connect to MongoDB cluster
client = MongoClient(MONGODB_URI,tlsCAFile=certifi.where())

#create a new database in the cluster called mlb_players
mlbDB = client['mlb_players']
mlb_collection = mlbDB['players']
# mlb_collection.insert_one({'name':"Ohtani",
#                            "BA": .345})

#get the id of Ohtani..
entry1 =mlb_collection.find_one({'name':"Ohtani"})
pprint(entry1)

mlb_collection.update_one({'name':'Ohtani'},{
    '$set':{'hr':45
            'rbi':0
            'sb':0,}
})
# for db_info in client.list_database_names():
#     print(db_info)
print("end of file..")