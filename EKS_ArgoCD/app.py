from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="mysql-server",
    user="root",
    password="password",
    database="testdb"
)

cursor = db.cursor()

@app.route('/add', methods=['POST'])
def add_data():
    name = request.json.get('name')
    cursor.execute(f"INSERT INTO test_table (name) VALUES ('{name}')")
    db.commit()
    return jsonify({"message": "Data added"}), 201

@app.route('/get', methods=['GET'])
def get_data():
    cursor.execute("SELECT * FROM test_table")
    result = cursor.fetchall()
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')