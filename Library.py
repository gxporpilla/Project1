import sqlite3
with sqlite3.connect("main.db") as db:            
    cursor = db.cursor()

class Library:
    
    with sqlite3.connect("main.db") as db:            
        cursor = db.cursor()

    def __init__(self):
        self.appId = None
        self.gameName = None
        self.release = None
        self.developer = None
        self.categories = None 
        self.genre = None
        self.tags = None
        self.price = None

    def getGameData(self, appid):
        find_game = ("SELECT * FROM GAMES WHERE APPID =?")
        cursor.execute(find_game, [(appid)])
        results = cursor.fetchone()
        if results:
            self.appId = results[1]
            self.gameName = results[2]
            self.release = results[3]
            self.developer = results[4]
            self.categories = results[5]
            self.genre = results[6]
            self.tags = results[7]
            self.price = results[8]
        

    def getPrice(self):
        return self.getPrice
    

    def printAll(self):
        print("\nApp ID: ", self.appId)
        print("Title: ", self.gameName)
        print("Release Date: ", self.release)
        print("Developer: ", self.developer)
        print("Categories: ", self.categories)
        print("Genre: ", self.genre)
        print("Tags: ", self.tags)
        print("Price: ", self.price)

    
