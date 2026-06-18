claims = [
    {"claim_id": "C001", "amount": 25000, "status": "approved"},
    {"claim_id": "C002", "amount": 70000, "status": "pending"},
    {"claim_id": "C003", "amount": 10000, "status": "approved"},
    {"claim_id": "C004", "amount": 90000, "status": "pending"}
]

pending_count = 0
pending_total = 0

for claim in claims:
    if claim["status"] == "pending":
        pending_count = pending_count + 1
        pending_total = pending_total + claim["amount"]

print("Pending claim count:", pending_count)
print("Pending total amount:", pending_total)        