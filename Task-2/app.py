from flask import Flask, render_template, request, redirect, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# MongoDB connection
client = MongoClient(os.getenv("MONGO_URI"))
db = client["todoDB"]
collection = db["items"]

@app.route("/")
def home():
    return render_template("todo.html")

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    try:
        itemName = request.form["itemName"]
        itemDescription = request.form["itemDescription"]

        collection.insert_one({
            "itemName": itemName,
            "itemDescription": itemDescription
        })

        return "To-Do Item submitted successfully!"
    except Exception as e:
        return f"Error: {e}"

@app.route("/data")
def get_items():
    items = list(collection.find({}, {"_id": 0}))
    return jsonify(items)

if __name__ == "__main__":
    app.run(debug=True)
