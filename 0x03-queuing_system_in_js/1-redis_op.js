import { createClient, print } from 'redis';

// Create a Redis client
const client = createClient({
  host: '127.0.0.1',
  port: 6379
});

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
  function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
      if (err) {
        console.error(`Error retrieving value for ${schoolName}: ${err.message}`);
        return;
      }
      console.log(reply);
    });
  }
  
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');