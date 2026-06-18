def summarize_claims(claims):
    approved_count = 0
    approved_total = 0

    pending_count = 0
    pending_total = 0

    rejected_count = 0
    rejected_total = 0

    for claim in claims:
        if claim["status"] == "approved":
            approved_count = approved_count + 1
            approved_total = approved_total + claim["amount"]

        elif claim["status"] == "pending":
            pending_count = pending_count + 1
            pending_total = pending_total + claim["amount"]

        elif claim["status"] == "rejected":
            rejected_count = rejected_count + 1
            rejected_total = rejected_total + claim["amount"]

    print("Approved claim count:", approved_count)
    print("Approved total amount:", approved_total)
    print("Pending claim count:", pending_count)
    print("Pending total amount:", pending_total)
    print("Rejected claim count:", rejected_count)
    print("Rejected total amount:", rejected_total)


claims = [
    {"claim_id": "C001", "amount": 25000, "status": "approved"},
    {"claim_id": "C002", "amount": 70000, "status": "pending"},
    {"claim_id": "C003", "amount": 10000, "status": "approved"},
    {"claim_id": "C004", "amount": 90000, "status": "pending"},
    {"claim_id": "C005", "amount": 50000, "status": "rejected"}
]

summarize_claims(claims)