import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';


const app = express();
const redisClient = createClient();
const redisGet = promisify(redisClient.get).bind(redisClient);
const redisSet = promisify(redisClient.set).bind(redisClient);

const listProducts = [
{Id: 1, name: 'Suitcase 250', price: 50, stock: 4},
{Id: 2, name: 'Suitcase 450', price: 100, stock: 10},
{Id: 3, name: 'Suitcase 650', price: 350, stock: 2},
{Id: 4, name: 'Suitcase 1050', price: 550, stock: 5}
];


function getItemById(id) {
  for (const item of listProducts) {
    if (id === item.Id) return {...item};
  }
  return null;
}


function reserveStockById(itemId, stock) {
  redisSet(itemId, stock)
  .then(data => data)
  .catch(()=>{});
}


async getCurrentReservedStockById(itemId) {
  const ans = await redisGet(itemId);
  return ans;
}

app.get('/list_products', (req, res) => {
  const items = listProducts.map(({Id, name, price, stock})=> ({
    itemId: Id, itemName: name, price,
    initialAvailabilityQuantity: stock}));
  res.send(JSON.stringify(items));
});

app.listen(1245,() => console.log('server running'));
