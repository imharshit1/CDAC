from flask import Flask,jsonify
app = Flask(__name__)

employees = [
    {
        "id": 101,
        "name": "Rahul",
        "department": "IT"
    },
    {
        "id": 102,
        "name": "Priya",
        "department": "HR"
    },
    {
        "id": 103,
        "name": "Arun",
        "department": "Finance"
    }
]
@app.route("/")
def home():
    return "Employee Management API is running!"

@app.route("/employees")
def get_employees():
    return jsonify(employees)

if(__name__=="__main__"):
    app.run(host="0.0.0.0", port = 5000)