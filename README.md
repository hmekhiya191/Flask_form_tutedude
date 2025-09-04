# Flask + MongoDB Atlas Project  

## 📌 Project Overview  
This project demonstrates the integration of **Flask** with **MongoDB Atlas**.  
It includes:  
- A Flask API route (`/api`) that reads data from a backend file and returns it as JSON.  
- A frontend form that submits user data to MongoDB Atlas.  
- A success page to confirm data submission.  
- A route (`/data`) that fetches and displays all stored MongoDB records.  

---

## ⚙️ Tech Stack  
- **Flask** (Python Web Framework)  
- **MongoDB Atlas** (Cloud Database)  
- **HTML / CSS** (Frontend form)  
- **pymongo** (MongoDB client for Python)  
- **dotenv** (for environment variable management)  

---


## 📌 Project Overview  
This repository contains two tasks organized into separate folders:  

- **Task 1 (components/task-1)** → A Flask API that reads from a JSON file (`data.json`) and returns the data via the `/api` route.  
- **Task 2 (components/task-2)** → A Flask + MongoDB integration where users can submit data via a form, store it in **MongoDB Atlas**, and view stored records using `/data`.  

---

## How to Run Task-1:

Open terminal.

Go to the folder components/task-1 using: cd components/task-1

Run the Flask app with: python app.py

Open browser and go to http://127.0.0.1:5000/api

You will see JSON data displayed from data.json file.

------------------

## How to Run Task-2:

Open terminal.

Go to the folder components/task-2 using: cd components/task-2

Make sure you have a .env file inside task-2 with your MongoDB connection string like:
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/myDatabase

Install the required dependencies using: pip install -r requirements.txt

Run the Flask app with: python app.py

Open browser and go to http://127.0.0.1:5000/
 to see the form.

After submitting the form, it will store data in MongoDB and redirect to a success page.

You can also visit http://127.0.0.1:5000/data
 to see the stored records from MongoDB.