import os
import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

def get_mysql_info(host, port, username, password):
    try:
        # Connect to the MySQL instance
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=username,
            password=password
        )

        cursor = connection.cursor()

        # Get information about MySQL instances
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()

        cursor.close()
        connection.close()

        return [db[0] for db in databases]

    except mysql.connector.Error as error:
        print("Error connecting to MySQL:", error)
        return []

@app.route("/mysql-instances")
def mysql_instances():
    # Read MySQL connection details from environment variables
    host = os.environ.get("MYSQL_HOST")
    port = int(os.environ.get("MYSQL_PORT", 3306))
    username = os.environ.get("MYSQL_USERNAME")
    password = os.environ.get("MYSQL_PASSWORD")

    if not all((host, username, password)):
        return jsonify({"error": "Please set MYSQL_HOST, MYSQL_USERNAME, and MYSQL_PASSWORD environment variables."}), 500
    else:
        instances = get_mysql_info(host, port, username, password)
        return jsonify({"mysql_instances": instances})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
