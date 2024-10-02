import mysql.connector

users = []
currentScreenName = ""

connection = mysql.connector.connect(
    port= 3306,
    host="localhost",
    user="root",
    password="password",
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
    currentScreenName = (input("Enter your name: "))

    getusers()

    ## In case is a new user, username added to database.
    if not checkscreenname():
        sql =f"INSERT INTO game (screen_name, id) VALUES ('{currentScreenName}', {len(users)+1}, {5})"
        cursor = connection.cursor()
        cursor.execute(sql)



def getHighestScore():
    global currentScreenName
    sql = f"SELECT highest_score FROM game WHERE screen_name = '{currentScreenName}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
       return print(row[0])


def getLatestScore():
    global currentScreenName
    sql = f"SELECT latest_score FROM game WHERE screen_name = '{currentScreenName}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
         return print(row[0])




addusername()
getHighestScore()
getLatestScore()