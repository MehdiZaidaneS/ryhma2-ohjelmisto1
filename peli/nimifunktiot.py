import mysql.connector

users = []
currentScreenName = ""

connection = mysql.connector.connect(
    port= 3306,
    host="localhost",
    user="alek",
    password="1234",
    database="flight_game",
    autocommit=True
)


def getusers(): #Getting all the users of the game.
    sql = f"SELECT * FROM game"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        users.append(row)


def checkscreenname(): #Checking if the username already exists on the database.
    screennames = []

    for i in users:
        screennames.append(i[4])

    if currentScreenName not in screennames:
        return False
    else:
        return True



def addusername():
    ## Setting the name of the player
    global currentScreenName
    currentScreenName = (input("Tervetuloa Maapallo peliin!\nSyötä nimesi: "))

    getusers()

    ## In case is a new user, username added to database.
    if not checkscreenname():
        sql =f"INSERT INTO game (screen_name, id, highest_score, latest_score) VALUES ('{currentScreenName}', {len(users)+1}, {0}, {0})"
        cursor = connection.cursor()
        cursor.execute(sql)

    return print(f"Korkein pistemäärä on: {getHighestScore()}\nViimeisin tulos on: {getLatestScore()}\n")


def getHighestScore():
    global currentScreenName
    sql = f"SELECT highest_score FROM game WHERE screen_name = '{currentScreenName}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
       return row[0]


def getLatestScore():
    global currentScreenName
    sql = f"SELECT latest_score FROM game WHERE screen_name = '{currentScreenName}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
         return row[0]


def addHighestScore(score):
    global currentScreenName
    if score > getHighestScore():
        sql = f"UPDATE game SET highest_score = {score} WHERE screen_name = '{currentScreenName}'"
        cursor = connection.cursor()
        cursor.execute(sql)


def addLatestScore(score):
    global currentScreenName
    sql= f"UPDATE game SET latest_score = {score} WHERE screen_name = '{currentScreenName}'"
    cursor = connection.cursor()
    cursor.execute(sql)



