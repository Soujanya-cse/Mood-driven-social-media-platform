from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)

# MongoDB connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/moodsocial"
mongo = PyMongo(app)
db = mongo.db  # Access the database

@app.route('/')
def home():
    return "Flask Backend is Running with MongoDB!"

# Signup route
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    if not data.get("username") or not data.get("password"):
        return jsonify({"error": "Missing fields"}), 400
    
    if db.users.find_one({"username": data["username"]}):
        return jsonify({"error": "User already exists"}), 400

    hashed_password = generate_password_hash(data["password"])
    
    try:
        db.users.insert_one({"username": data["username"], "password": hashed_password})
        print("✅ User signed up:", data["username"])  # Debugging log
        return jsonify({"message": "Signup successful"})
    except Exception as e:
        print("❌ MongoDB Error:", e)
        return jsonify({"error": "Database error"}), 500

# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = db.users.find_one({"username": data["username"]})
    
    if user and check_password_hash(user["password"], data["password"]):
        print("✅ User logged in:", data["username"])  # Debugging log
        return jsonify({"message": "Login successful"})
    else:
        print("❌ Login failed:", data["username"])  # Debugging log
        return jsonify({"error": "Invalid username or password"}), 401

if __name__ == '__main__':
    app.run(debug=True)
