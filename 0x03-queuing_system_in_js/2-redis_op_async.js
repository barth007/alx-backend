import redis  from 'redis';
import {promisify} from 'util';



const client  = redis.createClient()
client.on('Connect', ()=> {
  console.log("Connected to redis");
})
client.on('error', err=> console.error("Redis client not connected to the server:", err));
const setAsync = promisify(client.set).bind(client);
async function setNewSchool(schoolName, value) {
  try {
    await setAsync(schoolName, value);
    console.log(`value set for ${schoolName}`)
  } catch(error) {
    console.log('Error Message: ', error);
  } finally {
    client.quit();
  }
}
const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (error) {
    console.log('Error Message: ', error);
  } finally {
    client.quit();
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
