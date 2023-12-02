import redis  from 'redis';



const client  = redis.createClient()
client.on('Connect', ()=> {
  console.log("Connected to redis");
  client.quit();
})
client.on('error', err=> console.error("Redis client not connected to the server:", err));

//try{
  //const client = redis.createClient()
  //client.on('Connect', ()=> {
    //console.lgo("connected to redis");
    //client.quit();
  //})
//} catch(err) {
  //console.error("Redis client not connected to the server:,", err);
//}

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print)
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, redis.print)
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
