def summarize_claims(claims):
    summary = {}

    for claim in claims:
        status = claim["status"]
        amount = claim["amount"]

        if status not in summary:
            summary[status] = {
                "count": 0,
                "total": 0
            }

        summary[status]["count"] = summary[status]["count"] + 1
        summary[status]["total"] = summary[status]["total"] + amount

    return summary


claims = [
    {"claim_id": "C001", "amount": 25000, "status": "approved"},
    {"claim_id": "C002", "amount": 70000, "status": "pending"},
    {"claim_id": "C003", "amount": 10000, "status": "approved"},
    {"claim_id": "C004", "amount": 90000, "status": "pending"},
    {"claim_id": "C005", "amount": 50000, "status": "rejected"},
    {"claim_id": "C006", "amount": 30000, "status": "cancelled"}
]

result = summarize_claims(claims)

for status, data in result.items():
    print(status, "claim count:", data["count"])
    print(status, "total amount:", data["total"])