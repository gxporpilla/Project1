import stdiomask 
import getpass
import sqlite3, time
from Library import Library

with sqlite3.connect("main.db") as db:            
    cursor = db.cursor()

class User: 
    

    with sqlite3.connect("main.db") as db:
        cursor = db.cursor()

    def __init__(self, username, password, balance):
        self.username = username 
        self.password = password
        self.balance = balance
        
    def getUsername(self, username):
        return '{}'.format(username)

    def getPassword(self, password):
        return '{}'.format(password)

    def getBalance(self, balance): 
        return '{}'.format(balance)

    def __del__(self):
        print("Have a nice day!")

    """
    def login(self, un, pw):
        while True:
            userData = None
            find_user = ("SELECT * FROM ACCOUNTS WHERE username = ? AND password = ?")
            cursor.execute(find_user,[(un), (pw)])
            results = cursor.fetchall()
                
            if results:
                for i in results:
                    self.username = i[0]
                    self.balance = i[2]
                    print("\nWelcome {}!".format(self.username))
                    print("Balance:", self.balance)
                    return("exit")

            else:
                print("\nUsername and password not recognised")
                again = input("Do you want to try again? (y/n): ")
                if again.lower() == "n":
                    print("\nThank you and have a nice day!")
                    time.sleep(1)
    """

    def login(self, un, pw):
        while True:
            find_user = ("SELECT * FROM ACCOUNTS WHERE username = ? AND password = ?")
            cursor.execute(find_user,[(un), (pw)])
            results = cursor.fetchall()
            return results

    def loginCheck(self, un, pw):
        while True:
            results = self.login(un, pw)
            if results:
                for i in results:
                    self.username = i[0]                
                    self.balance = i[2]
                    print("\nWelcome {}!".format(self.username))
                    print("Balance:", self.balance)
                return 1

            else:
                print("\nUsername and password not recognised")
                again = input("Do you want to try again? (y/n): ")
                if again.lower() == "n":
                    print("\nThank you and have a nice day!")
                    time.sleep(1)
                    return ("exit")
                elif again.lower() == "y":
                    un = input("\nUsername: ")
                    pw = stdiomask.getpass()
                    self.login(un, pw)
                
    def reinitializeLogin(self, un, pw):
        find_user = ("SELECT * FROM ACCOUNTS WHERE username = ? AND password = ?")
        cursor.execute(find_user,[(un), (pw)])
        results = cursor.fetchall()
        for i in results:
            self.username = i[0]                
            self.balance = i[2]

    def signUp(self, newun, newpw):
        while True:
            find_user = ("SELECT * FROM ACCOUNTS WHERE username = ? AND password = ?")
            cursor.execute(find_user,[(newun), (newpw)])
            results = cursor.fetchall()
            return results

    def signupCheck(self, newun, newpw):
        while True:
            results = self.signUp(newun, newpw)
            if results:
                for i in results:
                    inputtedUn = newun
                    inputtedPw = newpw
                    
                    if i[0] == inputtedUn and i[1] == inputtedPw:
                        print("Sorry, but the user details exist. Please try again")
                    
            else:
                new_user = ("""INSERT INTO ACCOUNTS (USERNAME, PASSWORD, BALANCE) 
                                VALUES(?, ?, ?)""")
                defaultBal = 0
                cursor.execute(new_user,[(newun), (newpw), (defaultBal)])
                db.commit()
                print("bruh")
            return("exit")

    def buy(self, aId):
        g = Library()
        g.getGameData(aId)
        price = g.price
        bal = self.balance
        fPrice = float(price)
        if price <= bal:
            self.balance = bal - price
            bal = round(self.balance, 2)
            update_bal = ("UPDATE ACCOUNTS SET BALANCE = ? WHERE USERNAME = ?")
            cursor.execute(update_bal, [(bal), (self.username)])
            add_to_lib = ("""INSERT INTO ORDERS (APPID, USERNAME) 
                            VALUES (? ,?) """)
            cursor.execute(add_to_lib, [(aId), (self.username)])
            db.commit()
            print("Transaction Success! Happy Gaming!")
        else:
            print("Sorry, you do not have enough balance to make the purchase.")
            return 0

    def topup(self, amount):
        self.balance = self.balance + float(amount)
        topup_amt = ("UPDATE ACCOUNTS SET BALANCE = ? WHERE USERNAME = ?")
        cursor.execute(topup_amt, [(self.balance), (self.username)])
        print("Top Up Success! Your balance is now: ", self.balance)
        db.commit()

    def showMyLib(self):
        find_lib = ("SELECT APPID FROM ORDERS WHERE USERNAME = ?")
        cursor.execute(find_lib, [(self.username)])
        results = cursor.fetchall()
        if results is None:
            print("Nothing here. Browse the store to buy!")
        else:
            print("Your Library: \n")
            for i in results:
                l = Library()
                input = i[0]
                l.getGameData(input)
                print(l.gameName)


        





        

    


                
                



