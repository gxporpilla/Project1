from Library import Library
from user import User
import sqlite3
with sqlite3.connect("main.db") as db:            
    cursor = db.cursor()
class Store:
    
    with sqlite3.connect("main.db") as db:            
        cursor = db.cursor()

    def __init__(self):
        None

    def displayGames(self, username, password): 
        select =None
        next = 'y'
        count = 10
        while next.lower() == "y":
            count1 = (count-10)
            cursor.execute("SELECT AppID, NAME, TAGS FROM GAMES WHERE rowid BETWEEN ? and ?", (count1,count))
            items=cursor.fetchall()
            print("""AppID \t Title \t \t \t \t Tags""")
            for i in items:
                item1 = i[0]
                item2 = i[1]
                item3 = i[2]
                print(item1, "\t", item2, "\t \t \t \t", item3)
            select = input("Found something you want to view? Enter the AppID to view the game, or enter 'n' if none \t")
            sLow = select.lower()

            if sLow == "n":
                next = input("Next page? [y/n] \n")
                if next.lower() == "y":
                    count += 10
                elif next.lower() == "n":
                    break
            else: 
                l = Library()
                select = int(select)
                results = l.getGameData(select)
                if results is None:
                    l.printAll()
                    r = input("Enter '1' to buy the game, or enter '0' to go back to main menu \t")
                    print("\n")
                    if r == "1":
                        user = User(None, None, None)
                        user.reinitializeLogin(username, password)
                        user.buy(select)
                    else:
                        return 0
                else:
                    print("Game not found, redirecting to main menu. ")
                    print("\n")
                    return 0
                    

#FOR PRICE SEARCH 
    def getPrice(sPrice):
        sPrice=input("Price Range: ")
        print(" ")

        return sPrice
    
    def searchPrice(self):
        priceSearch=self.getPrice() 
        cursor.execute('SELECT * FROM GAMES WHERE PRICE <= ?', (priceSearch,))
        results = cursor.fetchall()
        print("""AppID \t Title""")
        for item in results:
            print(item[1], "\t", item[2])

        resp = input("Enter the specific number (appID) to view the game, or enter '0' to exit search \t")
        if resp != "0":
            game = Library()
            resp = int(resp)
            results = game.getGameData(resp)
            if results is None:

                game.printAll()
                r = input("Enter '1' to buy the game, or enter '0' to go back to main menu")
                if r == "1":
                    return resp
                else:
                    return 0
            else:
                r = input("Game not found, try again? [y/n]: \n")
                if r.lower() == "y":
                    self.searchPrice()
                else:
                    return 0
        else:
            return 0


#FOR GENRE SEARCH

    def getGenre(self):
        print("\nNOTE: For more than one genre, add a semicolon (;)")
        genre=input("Genre: ")
        print(" ")

        return genre
    
    def searchGenre(self):
        genreSearch=self.getGenre() 
        cursor.execute('SELECT * FROM GAMES WHERE GENRES LIKE ?', (genreSearch,))
        results = cursor.fetchall()
        print("""AppID \t Title""")
        for item in results:
            print(item[1], "\t", item[2])

        resp = input("Enter the specific number (appID) to view the game, or enter '0' to exit search \t")
        if resp != "0":
            game = Library()
            resp = int(resp)
            results = game.getGameData(resp)
            if results is None:

                game.printAll()
                r = input("Enter '1' to buy the game, or enter '0' to go back to main menu \t")
                if r == "1":
                    return resp
                else:
                    return 0
            else:
                r = input("Game not found, try again? [y/n]: ")
                if r.lower() == "y":
                    self.searchGenre()
                else:
                    return 0
        else:
            return 0


#FOR CATEGORY SEARCH
    def getCategory(self):
        print("\nNOTE: For more than one category, add a semicolon (;)")
        category=input("Category: ")
        print(" ")

        return category
    
    def searchCategory(self):
        categorySearch=self.getCategory() 
        cursor.execute('SELECT * FROM GAMES WHERE CATEGORIES LIKE ?', (categorySearch,))
        results = cursor.fetchall()
        print("""AppID \t Title""")
        for item in results:
            print(item[1], "\t", item[2])

        resp = input("Enter the specific number (appID) to view the game, or enter '0' to exit search \t")
        if resp != "0":
            game = Library()
            resp = int(resp)
            results = game.getGameData(resp)
            if results is None:

                game.printAll()
                r = input("Enter '1' to buy the game, or enter '0' to go back to main menu \t")
                if r == "1":
                    return resp
                else:
                    return 0
            else:
                r = input("Game not found, try again? [y/n]: ")
                if r.lower() == "y":
                    self.searchCategory()
                else:
                    return 0
        else:
            return 0


