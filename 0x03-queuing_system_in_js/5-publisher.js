import { createClient } from 'redis';

const channel = 'holberton school channel';
const client = createClient();

client.on('error', error => console.log(`Redis client not connected to the server: ${error}`));
client.on('ready', () => {
  console.log('Redis client connected to the server');
});

function publishMessage (message, time) {
  const timer = setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish(channel, message);
    clearTimeout(timer);
  }, time);
}

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
