import { createClient, print } from 'redis';


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

// Subscribe to the channel
client.subscribe('holberton school channel');

// Handle messages received on the subscribed channel
client.on('message', (channel, message) => {
  console.log(message);

  // Check if message is KILL_SERVER
  if (message === 'KILL_SERVER') {
    // Unsubscribe and quit Redis client
    client.unsubscribe();
    client.quit();
  }
});
