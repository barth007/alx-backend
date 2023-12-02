import redis  from 'redis';



const client  = redis.createClient()
client.on('Connect', ()=> {
  console.log("Connected to redis");
  client.quit();
})
client.on('error', err=> console.error("Redis client not connected to the server:", err));
