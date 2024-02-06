import { createClient } from 'redis';

(async () => {
  await createClient()
    .on('error', error => console.log(`Redis client not connected to the server: ${error}`))
    .on('ready', () => console.log('Redis client connected to the server'));
})()
  .catch((err) =>console.log(err));
