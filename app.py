from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import psycopg2.extras
import json
import os 

app = Flask(__name__)
CORS(app)


db_host = "127.0.0.1"
db_port = 5432
db_name = "phonebookdb"
db_user = "postgres"
db_password = os.environ.get("DB_PASSWORD", "")

def create_connection():
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        database=db_name,
        user=db_user,
        password=db_password
    )
    return conn

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/contacts/<contact_id>", methods=["GET"])
def get_data_single(contact_id):
    try:
        conn = create_connection()
        cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

        # Fetch data from the database
        cur.execute(f"SELECT id,  first_name, last_name, description, phone FROM contacts where id = {contact_id}")
        data = cur.fetchall()
 
        cur.close()
        conn.close()
    
        return jsonify(data)
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return jsonify({"error": "Failed to fetch data"})


@app.route("/contacts", methods=["GET"])
def get_data():
    try:
        conn = create_connection()
        cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

        # Fetch data from the database
        cur.execute("SELECT id,  first_name, last_name, description, phone FROM contacts")
        data = cur.fetchall()
 
        cur.close()
        conn.close()
    
        return jsonify(data)
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return jsonify({"error": "Failed to fetch data"})


@app.route("/contacts", methods=["POST"])
def store_data():
    data = request.get_json()
    first_name = data["first_name"]
    last_name = data["last_name"]
    description = data["description"]
    phone = data["phone"]

    try:
        conn = create_connection()
        cur = conn.cursor()

        # Insert data into the database
        cur.execute("INSERT INTO CONTACTS (first_name, last_name, description, phone) VALUES (%s, %s, %s, %s)",
                    ( first_name, last_name, description,phone ))
        conn.commit()

        cur.close()
        conn.close()

        return jsonify({"message": "Data stored successfully"})
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return jsonify({"error": "Failed to store data"})

@app.route("/contacts/<contact_id>", methods=["PUT"])
def update_data_single(contact_id):
    data = request.get_json()
    first_name = data["first_name"]
    last_name = data["last_name"]
    description = data["description"]
    phone = data["phone"]

    try:
        conn = create_connection()
        cur = conn.cursor()

        # Insert data into the database
        cur_stmt = f"UPDATE contacts set first_name =%s, last_name =%s, description =%s, phone=%s where id = {contact_id}"
        print (cur_stmt)
        cur.execute(cur_stmt,
                    ( first_name, last_name, description,phone ))
        conn.commit()

        cur.close()
        conn.close()

        return jsonify({"message": "Data stored successfully"})
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return jsonify({"error": "Failed to store data"})

@app.route("/contacts", methods=["PUT"])
def update_data():
    data = request.get_json()
    contact_id = data["id"]
    first_name = data["first_name"]
    last_name = data["last_name"]
    description = data["description"]
    phone = data["phone"]

    try:
        conn = create_connection()
        cur = conn.cursor()

        # Insert data into the database
        cur.execute("UPDATE contacts set first_name =%s, last_name =%s, description =%s, phone=%s where id = %s",
                    ( first_name, last_name, description,phone ,contact_id))
        conn.commit()

        cur.close()
        conn.close()

        return jsonify({"message": "Data stored successfully"})
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return jsonify({"error": "Failed to store data"})
    

@app.route("/contacts", methods=["DELETE"])
def delete_data():
    data = request.get_json()
    contact_id = data["id"]
    delete_data_single(contact_id)

    
@app.route("/contacts/<contact_id>", methods=["DELETE"])
def delete_data_single(contact_id):
    try:
        conn = create_connection()
        cur = conn.cursor()

        # Insert data into the database
        cur.execute(f"delete from contacts where id = {contact_id}")
        conn.commit()

        cur.close()
        conn.close()

        return jsonify({"message": "Data stored successfully"})
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return jsonify({"error": "Failed to store data"})
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
