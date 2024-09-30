import mysql.connector
from geopy.distance import distance
import math
import random


def randommaa():
    #arpoo etsittävän maan
    maat = (f"select name from country;")
    kursori = yhteys.cursor()
    kursori.execute(maat)
    maannimet = kursori.fetchall()
    #maannimet on nyt lista tupleja, en tiedä miksi joku sql juttu
    #lasketaan listan objektien määrä, arvotaan random luku tämän määrän sisällä
    #valitaan random luvun kohdalla oleva objekti maaksi
    #sitten vielä siistitään tuple stringiksi
    
    objektienmaara = len(maannimet)

    randomvalinta = random.randint(0,objektienmaara-1)

    valittumaa = maannimet[randomvalinta]

    #maan nimi oli aina tuplen ensimmäisessä indexissä:
    siistittyvalittumaa = valittumaa[0]

    return siistittyvalittumaa
    

def maanlentokenttienlokaatioidenkeskiarvo(maannimi):
    #funktio etsii tietokannasta kaikki parametriksi annetun maan lentokentät ja
    #laskee niiden lokaatioiden keskiarvon ja palauttaa tämän arvon 

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


def suunta(arvattumaa,tavoitemaa):
    #funktio suunta saa parametreiksi arvatun maan lokaation ja oikean maan lokaation
    #laskee maiden välisen kulman olettaen että pohjoinen on 0/360 etelä 180 jne
    #palauttaa kulman arvon
    


    return 0



yhteys = mysql.connector.connect(
    host="localhost",
    port= 3306,
    database="flight_game",
    user="user2",
    password="1234",
    autocommit=True
)



x = maanlentokenttienlokaatioidenkeskiarvo("Italy")
print(x)

print(randommaa())