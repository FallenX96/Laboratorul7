from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="password123",
        database="notite_vlad"
    )

@app.route("/")
def index():
    return "Salut de la aplicația Flask a lui Vlad!"

@app.route("/adauga", methods=["POST"])
def adauga():
    data = request.json["text"]
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notite (continut) VALUES (%s)", (data,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"status": "Notiță adăugată pentru Vlad!"})

@app.route("/notite", methods=["GET"])
def notite():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT continut FROM notite")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify([r[0] for r in rows])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)