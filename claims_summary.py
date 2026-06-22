# Function to summarize claims by status
def summarize_claims(claims):
    # Empty dictionary to store count and total for each status
    summary = {}

    # Loop through each claim one by one
    for claim in claims:
        status = claim["status"]
        amount = claim["amount"]

        # If status is coming for the first time, create it in summary
        if status not in summary:
            summary[status] = {
                "count": 0,
                "total": 0
            }

        # Increase count by 1 for that status
        summary[status]["count"] = summary[status]["count"] + 1

        # Add claim amount to total for that status
        summary[status]["total"] = summary[status]["total"] + amount

    # Return final summary dictionary
    return summary


# Claim data
claims = [
    {"claim_id": "C001", "amount": 25000, "status": "approved"},
    {"claim_id": "C002", "amount": 70000, "status": "pending"},
    {"claim_id": "C003", "amount": 10000, "status": "approved"},
    {"claim_id": "C004", "amount": 90000, "status": "pending"},
    {"claim_id": "C005", "amount": 50000, "status": "rejected"},
    {"claim_id": "C006", "amount": 30000, "status": "cancelled"}
]

# Call the function and store the result
result = summarize_claims(claims)

# Print count and total for each status
for status, data in result.items():
    print(status, "claim count:", data["count"])
    print(status, "total amount:", data["total"])