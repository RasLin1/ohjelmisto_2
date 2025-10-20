import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    port = 3306,
    database = "kk_flight_game",
    user="root",
    password=""
)


def search_airport(icao):
    query = f"SELECT type, count(*) AS amount FROM airport WHERE iso_country = %s GROUP BY type"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(query, (icao,))
        query_return = cursor.fetchall()
        if query_return:
            for row in query_return:
                print(f"Lentokentän tyypi: {row['type']} ja määrä on: {row['amount']}")
        else:
            print("Lentokenttä ei löytynyt")
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
    cursor.close()
    return True

search_keyword = input("Anna lentokentän ICAO koodi: ")
search = search_airport(search_keyword)
