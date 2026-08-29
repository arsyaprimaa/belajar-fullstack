const rawOrderData = `[
  {"orderId": 101, "customer": "Andi", "item": "Laptop Sleeve", "price": 150000, "status": "completed"},
  {"orderId": 102, "customer": "Budi", "item": "USB-C Hub", "price": 250000, "status": "pending"},
  {"orderId": 103, "customer": "Citra", "item": "Webcam HD", "price": 450000, "status": "completed"},
  {"orderId": 104, "customer": "Dewi", "item": "Mousepad Desk Mat", "price": 100000, "status": "cancelled"},
  {"orderId": 105, "customer": "Eka", "item": "Mechanical Switch", "price": 200000, "status": "completed"}
]`;

const orders = JSON.parse(rawOrderData);
const completedOders = orders.filter(item => item.status === "completed");
const customerList = completedOders.map(item => item.customer);
const totalRevenue = completedOders.reduce((acc, item) => acc + item.price, 0);
const playloadComleted = JSON.stringify(completedOders);

console.log("Customer List:", customerList);
console.log("Total Revenue:", totalRevenue);
console.log(playloadComleted);