import json

# 1. Simulasi Payload JSON yang dikirim oleh JavaScript/Frontend
raw_incoming_json = """[
  {"order_id": 101, "customer": "Andi", "item": "Mechanical Keyboard", "price": 750000, "is_paid": true},
  {"order_id": 102, "customer": "Budi", "item": "Wireless Mouse", "price": 350000, "is_paid": false},
  {"order_id": 103, "customer": "Citra", "item": "Monitor 24 Inch", "price": 1800000, "is_paid": true},
  {"order_id": 104, "customer": "Dewi", "item": "Desk Mat", "price": 100000, "is_paid": true}
]"""

# 2. DESERIALISASI: Mengubah string JSON menjadi Python List of Dictionaries
orders = json.loads(raw_incoming_json)

# 3. MANIPULASI DATA DENGAN PYTHON NATIVE

# A. FILTERING: Ambil transaksi yang sudah dibayar (is_paid == True)
paid_orders = [item for item in orders if item["is_paid"]]

# B. MAPPING: Ekstrak daftar nama pembeli dari transaksi yang sudah dibayar
paid_customers = [item["customer"] for item in paid_orders]

# C. AGREGASI / REDUCE: Hitung total penerimaan kas menggunakan built-in sum()
total_revenue = sum(item["price"] for item in paid_orders)

# 4. TAMPILKAN HASIL PROSES BACKEND
print("=== Output Backend Python ===")
print("Tipe data hasil parsing :", type(orders))
print("Jumlah pesanan lunas   :", len(paid_orders))
print("Daftar pelanggan lunas :", paid_customers)
print(f"Total Pendapatan       : Rp {total_revenue:,}")

# 5. SERIALISASI: Ubah data yang sudah difilter kembali ke JSON untuk response API
response_data = {
    "status": "success",
    "total_revenue": total_revenue,
    "paid_orders": paid_orders
}
json_response = json.dumps(response_data, indent=2)

print("\n=== Response JSON untuk Client/Frontend ===")
print(json_response)