from flask import Flask, jsonify

app = Flask(__name__)

database = {
    "user1" : { "name": "Alice", "age":35},
    "user2" : { "name": "Bob", "age":25}
}

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/users")
def get_all_users():
    users = []
    for user_id, user_data in database.items():
        user_name = user_data.get('name')
        if user_name is not None:
            users.append(user_data)

    return jsonify(users)

@app.route("/get_data/<key>", methods = ['GET'])
def get_data(key):
    if key in database:
        return jsonify(database[key])

    return jsonify({"error":f"{key} not found in database"})

app.run(debug=True)
