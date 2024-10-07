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
    if counter == 0:
        counter += 1
    
    latitude_keskiarvo = latitide_deg_summa/counter
    longitude_keskiarvo = longitude_deg_summa/counter




    return (latitude_keskiarvo, longitude_keskiarvo)


def suunta(arvattumaa,tavoitemaa):
    #funktio suunta saa parametreiksi arvatun maan lokaation ja oikean maan lokaation
    #laskee maiden välisen kulman olettaen että pohjoinen on 0/360 etelä 180 jne
    #palauttaa kulman arvon
    #https://www.igismap.com/formula-to-find-bearing-or-heading-angle-between-two-points-latitude-longitude/

    #latitudet ja longitudet täytyy nataa radiaaneissa
    lat1 = arvattumaa[0]*math.pi/180
    lat2 = tavoitemaa[0]*math.pi/180
    lon1 = arvattumaa[1]*math.pi/180
    lon2 = tavoitemaa[1]*math.pi/180
    x = math.cos(lat2)*math.sin(lon2-lon1)
    y = math.cos(lat1)*math.sin(lat2) - math.sin(lat1)*math.cos(lat2)*math.cos(lon2-lon1)

    bearing = math.atan2(y,x)
    # antaa bearing nyt radiaaneina välillä (pi ,-pi)

    return bearing


def ilmansuunta(kulmaradiaaneina):
    #funktio muuttaa suuntafunktion kulman ilmansuunnaksi
    #yksikköympyrä jaetaan kkuuteentoista samankokoiseen osaan
    #Ilmansuunta annetaan sen mukaan mihin osaan saatu kulmaradiaaneina osuu

    if -math.pi/8 <= kulmaradiaaneina < math.pi/8:
        return "idässä"
    if math.pi/8 <= kulmaradiaaneina < 3*math.pi/8:
        return "koillisessa"
    if 3*math.pi/8 <= kulmaradiaaneina < 5*math.pi/8:
        return "pohjoisessa"
    if 5*math.pi/8 <= kulmaradiaaneina < 7*math.pi/8:
        return "luoteessa"
    if -3*math.pi/8 <= kulmaradiaaneina < -math.pi/8:
        return "kaakossa"
    if -5*math.pi/8 <= kulmaradiaaneina < -3*math.pi/8:
        return "etelässä"
    if -7*math.pi/8 <= kulmaradiaaneina < -5*math.pi/8:
        return "lounaassa"
    if 7*math.pi/8 <= kulmaradiaaneina or kulmaradiaaneina <  -7*math.pi/8:
        return "lännessä"
    

    return 0

yhteys = mysql.connector.connect(
    host="localhost",
    port= 3306,
    database="flight_game",
    user="alek",
    password="1234",
    autocommit=True
)






print(maanlentokenttienlokaatioidenkeskiarvo("Egypt"))
print(maanlentokenttienlokaatioidenkeskiarvo("Estonia"))


testimuuttuja = suunta(maanlentokenttienlokaatioidenkeskiarvo("Japan"),maanlentokenttienlokaatioidenkeskiarvo("russia"))

print(testimuuttuja)

testimuuttuja2 = ilmansuunta(testimuuttuja)

print(testimuuttuja2)