console.log("from script.js...")
const MLBStatsAPI = require("mlb-stats-api")
const mlbStats = new MLBStatsAPI()



async function getData(){
    const result = await mlbStats.getPeople();
    console.log(result)
    console.log("end of getData")
}
getData()
console.log("end of script.js")