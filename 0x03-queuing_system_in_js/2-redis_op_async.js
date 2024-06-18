import { createClient, print } from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = createClient({
  host: '127.0.0.1',
  port: 6379
});

const getAsync = promisify(client.get).bind(client);
// Handle connection events
client.on('connect', () => {
    console.log('Redis client connected to the server');
  });
  
  client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
  });

  // Function to set a new school value in Redis
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
  }
  
  // Function to display the value of a school from Redis
  async function displaySchoolValue(schoolName) {
    try {
      const value = await getAsync(schoolName);
      console.log(value);
    } catch (error) {
      console.error(`Error retrieving value for ${schoolName}: ${error.message}`);
    }
  }

  (async () => {
    await displaySchoolValue('Holberton');
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
  })();