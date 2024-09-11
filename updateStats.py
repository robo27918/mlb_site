'''
TODO: 
    [x]get the stats from the mlb api
    [] set up a connection to the mongodb db
       and send the data over
'''
import mlbstatsapi
import os
import dotenv
import certifi
from pymongo import MongoClient
from dotenv import load_dotenv
import pprint
load_dotenv()
import json

MONGODB_URI = os.environ['MONGODB_URI']

mlb = mlbstatsapi.Mlb()

def getOhtaniStats():
    '''
        return the collection of all stats
        to be able to send it to mlb_players db
    '''
    
    #getting shohei player id
    shohei_id = mlb.get_people_id("Shohei Ohtani")

    #setting request variables
    stats =['season', 'seasonAdvanced']
    groups = ['hitting']
    params={"season":2024}

    #sending request
    sho_response = mlb.get_player_stats(
        int(shohei_id[0]),
        stats,
        groups,
        **params
    )
    sho_stats = sho_response['hitting']['season']

    sho_collection ={
        'homeruns':0,
        'avg':0,
        'stolenbases':0,
        'rbi':0
    }


    for split in sho_stats.splits:
        for k,v in split.stat.__dict__.items():
            if k in sho_collection:
                sho_collection[k] = v
    return sho_collection

print(getOhtaniStats())


def updateDb(updatedStats):
    print("from updateDb..")
    client = MongoClient(MONGODB_URI,tlsCAFile
                         =certifi.where()
                         )
    db =client['mlb_players']
    mlb_collection = db['players']
    # for collection in mlb_collection.find():
    #     print(collection)

    #
    set_update = {'$set': updatedStats}
    print(updatedStats)
    mlb_collection.update_one({'name':'Ohtani'}, set_update)
    
    for collection in mlb_collection.find():
        print(collection)


updateDb(getOhtaniStats())