from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get MongoDB URI from .env
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB Atlas
client = MongoClient(MONGO_URI)
db = client["myDatabase"]
collection = db["myCollection"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]

            # Insert into MongoDB
            collection.insert_one({"name": name, "email": email})

            # Redirect to success page
            return redirect(url_for("success"))

        except Exception as e:
            return render_template("form.html", error=str(e))

    return render_template("form.html")

@app.route("/success")
def success():
    return "Data submitted successfully ✅"

@app.route("/data")
def get_data():
    data = list(collection.find({}, {"_id": 0}))
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
