def total_spending(request_spending, account_id: str, category: str): #amt spent by acc in category
    for i in request_spending[account_id]['transactions']:
        if i['category'] == category:
            return i['amount']
        
def account_balance(request_spending, account_id: str):  #returns balance left (if any) else 0
    amt = request_spending[account_id]['balance'] 
    for i in request_spending[account_id]['transactions']:
        amt += i['amount']
    return amt if amt>0 else 0

def money_owed(request_spending, account_id: str): #returns expense that exceeds balance (if any) else 0
    amt = request_spending[account_id]['balance'] 
    for i in request_spending[account_id]['transactions']:
        amt += i['amount']
    return abs(amt) if amt<0 else 0

request_spending = {
    "Mahek": {
        "balance": 3000.00,
        "transactions": [
            {"amount": -9000.00, "category": "Creatives"},
            {"amount": 7000.00, "category": "Sponsor"},
            {"amount": -2000.00, "category": "Prize-Money"}
        ]
    },
    "Arham": {
        "balance": 5000.00,
        "transactions": [
            {"amount": 8000.00, "category": "Stalls"},
            {"amount": 7500.00, "category": "Seminars"}
        ]
    },
    "Unnati": {
        "balance": 3500.00,
        "transactions": [
            {"amount": -5000.00, "category": "Attraction"},
            {"amount": 2500.00, "category": "Promo"},
            {"amount": -900.00, "category": "Lighting"},
            {"amount": -3000.00, "category": "Games"}
        ]
    },
    "Gaurang": {
        "balance": 2000.00,
        "transactions": [
            {"amount": -1500.00, "category": "Website"},
            {"amount": -1000.00, "category": "C2C"},
            {"amount": -500.00, "category": "Posters"}
        ]
    }
}

print(total_spending(request_spending, 'Mahek', 'Creatives'))
print(account_balance(request_spending, 'Mahek'))
print(money_owed(request_spending, 'Mahek'))
