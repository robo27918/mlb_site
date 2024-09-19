const express = require("express");
const connectDB = require('./database/db')
const userRoutes = require("./routes/userRoutes");

//creates a new Express application, used to define applications settings, routes, middleware
// and HTTP request-handling
const app = express() 
const port = 3000;

//connect to the database
connectDB();

//serve static files from the public directory
app.use(express.static('public'))

//used to parese json from incoming requests
app.use(express.json());

//middleware is used to parse URL-encoded form data submitted via html
app.use(express.urlencoded({extended:true}))

//set the view enginge to EJS
// these two lines configue Express app to use
//EJS  templating engine to render dynamic HTML pages
app.set('view engine', 'ejs');
app.set('views', './views')




//mounts the router at the root path,meaning
//all the routes defined in userRoutes are now available
//from  root

//userRoutes is  a router module that defines multiple 
//routes for handling user related functionality
app.use('/',userRoutes)

//start the server
app.listen(port,(err) =>{
    if (err){
        console.log(err);
    }else{
        console.log(`Server is connected at port ${port}`)
    }
})
