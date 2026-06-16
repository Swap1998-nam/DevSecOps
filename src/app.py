import os
import subprocess
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Vulnerability 1: Command Injection
@app.route('/ping')
def ping():
    host = request.args.get('host')
    return subprocess.getoutput(f"ping -c 1 {host}")

# Vulnerability 2: SQL Injection
@app.route('/user')
def user():
    user_id = request.args.get('id')

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)

    result = cursor.fetchall()
    return str(result)

# Vulnerability 3: Hardcoded Secret
AWS_SECRET_KEY = "AKIA1234567890SECRET"

# Vulnerability 4: Unsafe Eval
@app.route('/calc')
def calc():
    expression = request.args.get('exp')
    return str(eval(expression))

if __name__ == "__main__":
    app.run(debug=True)
