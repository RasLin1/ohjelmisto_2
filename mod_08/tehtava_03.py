import mysql.connector
from geopy.distance import geodesic

db = mysql.connector.connect(
    host="127.0.0.1",
    port = 3306,
    database = "kk_flight_game",
    user="root",
    password=""
)

allow_program = True
comparable_airports = {}
cordinate_list = []

def search_airport(icao):
    query = f"SELECT name, latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    try: 
        cursor = db.cursor(dictionary=True)
        cursor.execute(query, (icao,))
        temp_holder = cursor.fetchall()
        query_return = temp_holder[0]
        if query_return:
            comparable_airports[icao] = {"name": query_return["name"], "lat": query_return["latitude_deg"], "lon": query_return["longitude_deg"]}
        else:
            print("Lentokenttä ei löytynyt")
    except mysql.connector.Error as err:
        print(f"Virhe: {err}")
    cursor.close()
    return True

while allow_program:
    if len(comparable_airports) < 2:
        search_keyword = input("Anna lentokentän ICAO koodi: ")
        search_normalised = search_keyword.upper()
        search = search_airport(search_normalised)
    elif len(comparable_airports) >= 2:
        for data in comparable_airports.values():
            temp_aiport_cordinate_tuple = (data["lat"], data["lon"])
            cordinate_list.append(temp_aiport_cordinate_tuple)
        final_distance = geodesic(cordinate_list[0], cordinate_list[1]).km
        final_distance_rounded = "%.2f" % final_distance
        print(f"Lopullinen etäisyys lentokenttien välillä on: {final_distance_rounded}km")
        allow_program = False


