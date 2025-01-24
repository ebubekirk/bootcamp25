from flask import Flask, jsonify, request, json
import datetime

app = Flask(__name__)


# Helper function to read transactions from the file
def read_transactions():
    try:
        with open("transactions.json", "r") as file:
            data = file.read()
            return eval(data)
    except FileNotFoundError:
        return []

# transactions
transactions = read_transactions()

# Helper function to write transactions to the file
def write_transactions(transactions):
    with open("transactions.json", "w") as file:
        json.dump(transactions, file)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    data = request.get_json()

    # Validate required fields
    required_fields = ["type", "amount", "category", "date"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Validate type
    if data["type"] not in ["income", "expense"]:
        return jsonify({"error": "Invalid type. Must be 'income' or 'expense'"}), 400

    # Validate amount
    try:
        data['amount'] = float(data['amount'])
    except ValueError:
        return jsonify({"error": "Amount must be a numeric value"}), 400

    # Validate category
    if data["category"] not in ["Food", "Rent", "Salary"]:
        return jsonify({"error": "Invalid category. Must be 'Food', 'Rent' or 'Salary'"}), 400

    # Validate date
    try:
        datetime.datetime.strptime(data['date'], "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "Invalid date format. Must be YYYY-MM-DD"}), 400

    # Append, and save transaction
    transactions.append(data)
    write_transactions(transactions)

    return jsonify({"message": "Transaction added successfully"}), 201

@app.route('/view_transactions', methods=['GET'])
def view_transactions():
    # Sort transactions by date
    sorted_transactions = sorted(transactions, key=lambda x: x["date"])
    return jsonify(sorted_transactions), 200

@app.route('/financial_summary', methods=['GET'])
def financial_summary():
    total_income = sum(t["amount"] for t in transactions if t["type"] == "income")
    total_expenses = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance = total_income - total_expenses

    summary = {
        "Total Income": total_income,
        "Total Expenses": total_expenses,
        "Remaining Balance": balance
    }

    return jsonify(summary), 200

app.run(debug=True)
