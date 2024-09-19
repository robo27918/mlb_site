const express = require('express');
const Player = require("../model/model")
//
const router = express.Router()

//Get route
router.get('/', async(req,res)=>{
    try{
        const players = await Player.find();
        console.log("from router.get....")
        console.log(players)
        
        res.render('index',{players});
    }catch(err){
        console.error('Error fetching user data:',err);
        res.status(500).render('index', {error: 'Error fetching users data', users:[]})
    }
    
})

///post goes below....

module.exports = router