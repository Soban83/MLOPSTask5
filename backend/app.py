from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# MongoDB connection URI
MONGODB_URI = "mongodb://localhost:27017/mlops"

# Connect to MongoDB
client = MongoClient(MONGODB_URI)
db = client["webapp"]
collection = db["users"]

@app.route('/store-info', methods=['POST'])
def store_info():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    collection.insert_one({'name': name, 'email': email})
    return jsonify({'message': 'Data stored successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
