from nimifunktiot import *
from peli import *

annetutmaat = 0
pisteet = 0



def start():
    global annetutmaat
    global pisteet
    #Peli alkaa siten, että pelaaja lisää käyttäjätunnuksen ja tallentaa sen tietokantaan.
    addusername()

    # While- loop ja PELI päättyy, kun pelaajalla on yhteensä viisi maata arvattavakseen.
    while annetutmaat < 5:
        #Peli asetti yhden satunnaisen maan ja lisäämme +1 maan joka kerta, kun maa annetaan.
        maa = randommaa()
        annetutmaat += 1
        yritykset = 5
        print(f"Arvaa sinun {annetutmaat}° maa!")

        # Pelaajalla on 5 yritystä arvata maa. Se päättyy, kun se saavuttaa 5 yritystä.
        while yritykset > 0:
            # Pelaaja syöttää maan nimen.
            maannimi = input("Syötä maan nimi: ")

            # Jos pelaaja arvaa oikein, hän saa pisteitä sen mukaan, kuinka monta yritystä hänellä oli.
            if maannimi == maa:
                print("Onnittelut, arvasit oikein!\n")
                pisteet= pisteet + yritykset * 10
                print(f"Voitit + {yritykset *10} pistettä!")
                print(f"Pisteet yhteensä: {pisteet}\n")
                break

            #Jos pelaaja arvaa väärin, se jatkuu, kunnes hän saavuttaa 5 yritystä.
            elif maannimi != maa:
                print(f"Väärin, yritä uudelleen! {yritykset-1} yritystä jäljellä.")

                #etäisyys maannimi ja maa välillä:a
                distancebetween = distance(maanlentokenttienlokaatioidenkeskiarvo(maa),maanlentokenttienlokaatioidenkeskiarvo(maannimi))
                print(f"Maiden välinen etäisyys {distancebetween}")

                if yritykset == 1:
                   print(f"Oikea maa oli {maa}.\n")

            

            yritykset -= 1


    #Peli päättyy pelaajan korkeimman ja viimeisimmän tuloksen näyttämiseen.
    addLatestScore(pisteet)
    addHighestScore(pisteet)
    print(f"Korkein pistemäärä on: {getHighestScore()}\nViimeisin tulos on: {getLatestScore()}\n")




start()