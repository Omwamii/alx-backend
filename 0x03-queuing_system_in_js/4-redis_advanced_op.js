import { createClient, print } from 'redis';

const client = createClient({
    host: '127.0.0.1',
    port: 6379
  });

client.on('connect', () => {
    console.log('Redis client connected to the server');
  });
  
  client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
  });

// Function to create and store a hash in Redis
function createHash() {
  client.hset("HolbertonSchools", "Portland", 50, print);
  client.hset("HolbertonSchools", "Seattle", 80, print);
  client.hset("HolbertonSchools", "New York", 20, print);
  client.hset("HolbertonSchools", "Bogota", 20, print);
  client.hset("HolbertonSchools", "Cali", 40, print);
  client.hset("HolbertonSchools", "Paris", 2, print);
}
  

  function displayHash() {
    client.hgetall("HolbertonSchools", (err, reply) => {
      if (err) {
        console.error(`Error retrieving hash values: ${err.message}`);
        return;
      }
      console.log(reply);
    });
  }

  createHash();
 displayHash();