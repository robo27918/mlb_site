/**
 * TODO: 
 *  [x]:connect to mongodb with node.js
 *  [x]: read ohtani data from mongodb
 *  []:get data from mongo db into schema using mongoose
 */

const {MongoClient} = require("mongodb")
const mongoose = require("mongoose");
//loading the contents of the environment file
require('dotenv').config()
//replacing the uri 
const uri = process.env.MONGODB_URI
const client = new MongoClient(uri,{tls:true});

// function to check connection
(async() =>{
    try{
        await client.connect();
        const dbRole = await client.db('mlb_players').command({hello:1});
        console.log(`Role of datebase - Host ${dbRole.me} Is primary: ${dbRole.isWriteablePrimary}`);

        const mlb_players = await client.db('mlb_players').collection('players') //.collection('other')
        const document = await mlb_players.findOne({'name':"Ohtani"});
        console.log(document)
        // console.log('data from collection ', mlb_players.findOne({'name:': "Ohtani"}))
        
        
        await client.close();
    }catch(e){
        console.log("Error", e.message)
    }
})();


//connecting to mongoDB via mongoose
const connectDB = async() =>{
    try{
        await mongoose.connect(uri,{})
    }catch(err){
        console.error("Error connecting to the database:",err);
        process.exit(1);
    }
}