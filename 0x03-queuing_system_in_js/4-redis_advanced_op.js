import redis  from 'redis';



const client  = redis.createClient()
client.on('Connect', ()=> {
  console.log("Connected to redis");
  client.quit();
})
client.on('error', err=> console.error("Redis client not connected to the server:", err));



client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools','seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

client.hgetall('HolbertonSchools', (error, reply) =>{
  if (error) {
    console.error('Error occurred while setting the value: ', error);
  } else {
    console.log('Hash retrieved: ', reply)
  }
})
client.quit()
//console.error("error for setting value: ", err)
