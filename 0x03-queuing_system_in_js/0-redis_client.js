import redis  from 'redis';



//const client  = redis.createClient()
//client.on('Connect', ()=> {
 // console.log("Connected to redis");
 // client.quit();
//})
//client.on('error', err=> console.error("Redis client not connected to the server:", err));

try{
  const client = redis.createClient()
  client.on('Connect', ()=> {
    console.lgo("connected to redis");
    //client.quit();
  })
} catch(err) {
  console.error("Redis client not connected to the server:,", err);
}
