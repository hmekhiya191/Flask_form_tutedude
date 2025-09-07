# Flask and MongoDB Assignment – Tasks 1 to 4

This repository contains four tasks that combine **Flask**, **MongoDB Atlas**, and **Git/GitHub** operations. The tasks cover building APIs, handling form submissions, integrating with MongoDB, and practicing advanced Git branching, merging, resetting, and rebasing.

---

## 📌 Task 1 – Flask API with JSON File
- Created a Flask application with an `/api` route.
- The route reads data from a backend file (`data.json`) and returns it as JSON.
- **Learning:** Basics of Flask routing and serving data from a file.

**How to Run:**
cd components/task-1
python app.py
Visit: http://127.0.0.1:5000/api

📌 Task 2 – Flask Form with MongoDB
Built a frontend form with fields for user input.
On submit, data is stored in MongoDB Atlas via Flask backend.
Success leads to a redirect page, errors remain on the form page.
Added a /data route to display stored records.
Learning: Flask + MongoDB integration and form handling.
How to Run:

bash
Copy code
cd components/task-2
# Add your MongoDB URI inside a .env file:
# MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/myDatabase
pip install -r requirements.txt
python app.py
Visit:
http://127.0.0.1:5000/ → Form page
http://127.0.0.1:5000/data → View MongoDB records

📌 Task 3 – Git Branching and Merging
Created two branches: master_1 and master_2.
master_1: Developed a frontend To-Do page with a form.
master_2: Created /submittodoitem backend route to store To-Do items in MongoDB.
Merged both branches into main.
Learning: Parallel development using Git branches and merging changes.

📌 Task 4 – Advanced Git (Reset and Rebase)
Enhanced the To-Do form in master_1 by adding:
Item ID
Item UUID
Item Hash
Each field was committed separately in sequence.
Merged into main, then used git reset --soft to roll back to the Item ID only commit.
Rebasing was performed to bring changes from main back into master_1.
Conflicts in todo.html were resolved manually.
Learning: Commit sequencing, Git reset, and Git rebase with conflict resolution.

📝 Summary
Through these tasks, I learned:
Flask basics: Creating APIs and handling routes.
MongoDB integration: Submitting and retrieving data via Flask backend.
Git branching & merging: Managing parallel development workflows.
Advanced Git operations: Using reset and rebase while preserving clean commit history.
This project gave me practical experience in full-stack development and version control workflows.