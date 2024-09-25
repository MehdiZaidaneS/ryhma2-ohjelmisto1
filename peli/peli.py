import mysql.connector
from geopy.distance import distance

def maanlentokenttienlokaatioidenkeskiarvo(maannimi):

    listalokaatioista = (f"select latitude_deg, longitude_deg from airport, country where airport.iso_country = country.iso_country and country.name = '{maannimi}';")
    kursori = yhteys.cursor()
    kursori.execute(listalokaatioista)
    maanlentokenttienlokaatiot = kursori.fetchall()

    latitide_deg_summa = 0
    longitude_deg_summa = 0
    counter = 0

    for i in maanlentokenttienlokaatiot:
        latitide_deg_summa = latitide_deg_summa + i[0]
        longitude_deg_summa = longitude_deg_summa + i[1]
        counter = counter + 1

    latitude_keskiarvo = latitide_deg_summa/counter
    longitude_keskiarvo = longitude_deg_summa/counter




    return (latitude_keskiarvo, longitude_keskiarvo)



yhteys = mysql.connector.connect(
    host="localhost",
    port= 3306,
    database="flight_game",
    user="user2",
    password="salasana",
    autocommit=True
)

x = maanlentokenttienlokaatioidenkeskiarvo("Italy")
print(x)