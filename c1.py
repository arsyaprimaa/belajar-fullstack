import json

raw_transactions = """[
  {"id": "TRX01", "buyer": "Rian", "category": "Elektronik", "amount": 1200000, "status": "settled"},
  {"id": "TRX02", "buyer": "Siti", "category": "Pakaian", "amount": 250000, "status": "pending"},
  {"id": "TRX03", "buyer": "Doni", "category": "Elektronik", "amount": 850000, "status": "settled"},
  {"id": "TRX04", "buyer": "Maya", "category": "Buku", "amount": 150000, "status": "cancelled"},
  {"id": "TRX05", "buyer": "Fajar", "category": "Elektronik", "amount": 3000000, "status": "settled"}
]"""


transactions = json.loads(raw_transactions)
settled_electronics = [order for order in transactions if order["status"] == "settled"  and order["category"] == "Elektronik"]
buyer_list = [order["buyer"] for order in settled_electronics]
total_settled_amount = sum(order["amount"] for order in settled_electronics)

response_payload = {
    "total_buyers": len(buyer_list),
    "total_amount": total_settled_amount,
    "buyers": buyer_list
}
json_response = json.dumps(response_payload, indent=2)
print(json_response)