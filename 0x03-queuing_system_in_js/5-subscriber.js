import { createClient } from 'redis';

const channel = 'holberton school channel';
const client = createClient();

client.on('error', error => console.log(`Redis client not connected to the server: ${error}`));
client.on('ready', () => {
  console.log('Redis client connected to the server');
});

client.on('message', (chnl, message) => {
  if (chnl === channel) {
    if (message === 'KILL_SERVER') {
      client.unsubscribe(channel);
      client.quit();
    }
    console.log(message);
  }
});
client.subscribe(channel);
