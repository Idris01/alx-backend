import { createClient, print } from 'redis';

const id = 'HolbertonSchools';
const info = ['Portland=50', 'Seattle=80', 'New York=20', 'Bogota=20', 'Cali=40', 'Paris=2'];
const client = createClient();
client.on('error', error => console.log(`Redis client not connected to the server: ${error}`));
client.on('ready', () => {
  console.log('Redis client connected to the server');
  for (const data of info) {
    const [key, field] = data.split('=');
    client.hset(id, key, field, print);
  }
  client.hgetall(id, (err, msg) => {
    if (!err) console.log(msg);
  });
});
