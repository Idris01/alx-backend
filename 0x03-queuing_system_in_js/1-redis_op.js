import { createClient, print } from 'redis';

const client = createClient();
client.on('error', error => console.log(`Redis client not connected to the server: ${error}`));
client.on('ready', () => {
  console.log('Redis client connected to the server');
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
});

function setNewSchool (schoolName, value) {
  client.set(schoolName, value, print);
}

function displaySchoolValue (schoolName) {
  client.get(schoolName, (err, reply) => {
    if (!err) console.log(reply);
  });
}
