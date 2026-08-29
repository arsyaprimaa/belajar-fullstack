// 1. Simulasi data mentah JSON yang diterima dari API/Server
const rawJsonData = `[
  {"id": 1, "name": "Mechanical Keyboard", "price": 750000, "category": "Accessories"},
  {"id": 2, "name": "Wireless Mouse", "price": 350000, "category": "Accessories"},
  {"id": 3, "name": "Monitor 24 Inch", "price": 1800000, "category": "Display"}
]`;

// 2. PARSING: Mengubah string JSON mentah menjadi Array/Object JavaScript
const products = JSON.parse(rawJsonData);

// 3. TRANSFORMASI DATA (Array Methods yang wajib dikuasai untuk interview)
// Filter: Ambil hanya produk dengan kategori 'Accessories'
const accessories = products.filter(item => item.category === "Accessories");

// Map: Ambil daftar nama produk saja
const productNames = products.map(item => item.name);

// Reduce: Hitung total nilai inventaris semua barang
const totalInventoryValue = products.reduce((acc, item) => acc + item.price, 0);

console.log("=== Hasil Parsing Data ===");
console.log("Aksesoris:", accessories);
console.log("Daftar Nama:", productNames);
console.log(`Total Nilai Inventaris: Rp ${totalInventoryValue.toLocaleString("id-ID")}`);

// 4. STRINGIFY: Mengubah kembali JS Object/Array menjadi string JSON (untuk dikirim ke backend)
const payloadKeBackend = JSON.stringify(accessories);
console.log("\nData siap kirim (JSON String):", payloadKeBackend);