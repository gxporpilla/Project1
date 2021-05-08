import stdiomask
import getpass
import sqlite3, time
from user import User

with sqlite3.connect("main db.db") as db:            
    cursor = db.cursor()

def getUsername(username):
    username = input("\nUsername: ")
    return username  

def getPassword(password):
    password = stdiomask.getpass()
    return password

def getBalance():
    while True:
        userData = None
        userName = getUsername(userData)
        passWord = getPassword(userData)
        find_user = ("SELECT * FROM ACCOUNTS WHERE username = ? AND password = ?")
        cursor.execute(find_user,[(userName), (passWord)])
        results = cursor.fetchall()
            
        if results:
            for i in results:
                print("\nWelcome {}!".format(userName))
                print("Balance:", i[2])
                return("exit")

        else:
            print("\nUsername and password not recognised")
            again = input("Do you want to try again? (y/n): ")
            if again.lower() == "n":
                print("\nThank you and have a nice day!")
                time.sleep(1)
                break 
                      
def login():
    getBalance()


welcomePrompt = "Welcome to Don Jose XP's Game library!"
print (welcomePrompt)
login()


      