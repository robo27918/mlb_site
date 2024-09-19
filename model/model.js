const mongoose = require('mongoose');
const Schema = mongoose.Schema

const playerSchema = new Schema ({
    name:{
        type:String,
        required:true,
    },
    avg:{
        type:String,
        required:true,
    },
    rbi:{
        type:String,
        required:true
    },
    homeruns:{
        type:String,
        required:true
    },
    stolenbases:{
        type:String,
        required:true
    },

},{collection:'players'});

const Player = mongoose.model('Player', playerSchema)
console.log("from model.js", Player)
module.exports = Player;