import math
import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route("/airport")



def search_airport():
    db = mysql.connector.connect(
    host="127.0.0.1",
    port = 3306,
    database = "kk_flight_game",
    user="root",
    password=""
    )
    query = f"SELECT name, municipality FROM airport WHERE ident = %s"
    try:
        args = request.args
        icao = str(args.get("icao"))
        cursor = db.cursor(dictionary=True)
        cursor.execute(query, (icao,))
        query_return = cursor.fetchone()
        response = {
            "ICAO": icao,
            "Name": query_return.name,
            "Municipality": query_return.municipality
        }
    except ValueError:
        response = {
            "result": "Virhe tapahtui ;("
        }
    return jsonify(response)

@app.errorhandler(404)
def page_not_found(virhe):
    response = {
        "result": virhe.result
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000) 
