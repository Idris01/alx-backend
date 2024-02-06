import { createClient, print } from 'redis';
import { promisify } from 'util';

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

async function displaySchoolValue (schoolName) {
  const get = promisify(client.get).bind(client);
  try {
    const data = await get(schoolName);
    console.log(data);
  } catch (error) {
    console.log(error);
  }
}
