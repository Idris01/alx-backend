import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
app.use(express.json());

const redisClient = createClient();
const redisGet = promisify(redisClient.get).bind(redisClient);
const redisIncr = promisify(redisClient.incrby).bind(redisClient);
const port = 1245;

const listProducts = [
  { Id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { Id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { Id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

function getItemById (id) {
  for (const item of listProducts) {
    if (id === item.Id) return { ...item };
  }
  return null;
}

function reserveStockById (itemId, stock) {
  redisIncr(`item.${itemId}`, stock)
    .then(data => data)
    .catch(() => {});
}

async function getCurrentReservedStockById (itemId) {
  const ans = await redisGet(`item.${itemId}`);
  return ans;
}

app.get('/list_products', (req, res) => {
  const items = listProducts.map(({ Id, name, price, stock }) => ({
    itemId: Id,
    itemName: name,
    price,
    initialAvailabilityQuantity: stock
  }));
  res.send(JSON.stringify(items));
});

app.get('/list_products/:itemId', async (req, res) => {
  const item = getItemById(+req.params.itemId);
  if (item) {
    const { Id: itemId, name: itemName, price, stock } = item;
    const reserved = await getCurrentReservedStockById(itemId);
    res.send(JSON.stringify({ itemId, itemName, price, initialAvailability: stock, currentQuantity: +stock - +reserved }));
  } else {
    res.send(JSON.stringify({ status: 'Product not found' }));
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const item = getItemById(+req.params.itemId);
  if (item && (+item.stock > +(await getCurrentReservedStockById(item.Id)))) {
    const { Id: itemId } = item;
    reserveStockById(itemId, 1);
    res.send(JSON.stringify({ status: 'Reservation confirmed', itemId }));
  } else if (item) {
    res.send(JSON.stringify({ status: 'Not enough stock available', itemId: item.Id }));
  } else {
    res.send(JSON.stringify({ status: 'Product not found' }));
  }
});

app.listen(port, () => console.log(`server running on port ${port}`));
