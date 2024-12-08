from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
app = Flask(__name__)
CORS(app)  # Enables CORS for all routes
# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["bis_integration"]
collection = db["restaurants"]

@app.route("/api/restaurants", methods=["GET"])
def get_restaurants():
    restaurants = list(collection.find({}, {"_id": 0}))  # Fetch all restaurants, excluding the _id field
    return jsonify(restaurants)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
