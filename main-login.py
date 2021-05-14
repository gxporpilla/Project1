import stdiomask
import getpass
import sqlite3, time
from user import User
from Library import Library
from Store import Store

with sqlite3.connect("main.db") as db:            
    cursor = db.cursor()

def promptUsername():
    username = input("\nUsername: ")
    return username  

def promptPassword():
    password = stdiomask.getpass()
    return password
    
def selectServices():
    print("\nChoose your preferred service below by inputting the corresponding number")
    print("1. Login")
    print("2. Sign-up")
    response = input("\nInput: ")
    if response == "1":
        loginService()
    elif response == "2":
        signupService()       
    return   

def loginService():

    un = promptUsername() #"Lee4an"              
    pw = promptPassword() #"as326159"            
    u = User(un, pw, 0)
    u.login(un, pw)
    x = u.loginCheck(un, pw)
    if x:
        mainMenu(un, pw, u)



    """
    games = Library()
    store = Store()
    store.searchGenre('Action')
    """

def signupService():
    print("Hello new user! Please enter your personal details below")
    newun = promptUsername()
    newpw = promptPassword()
    newu = User(newun, newpw, 0)
    newu.signUp(newun, newpw)
    newu.signupCheck(newun, newpw)
    print("Welcome, ", newun, ". Redirecting...")  
    selectServices()

def mainMenu(username, password, u):
    user = User(None, None, None)
    user.reinitializeLogin(username, password)
    l = Library()
    s = Store()
    resp = 1
    while resp:
        resp = input("""Please enter...
                        1 - View library
                        2 - Browse Store
                        3 - TopUp
                        4 - Search for games
                        5 - Logout \n""")
        if resp == "1":
            u.showMyLib()
        elif resp == "2":
            s.displayGames(username, password)
        elif resp == "3":
            amt = input("Enter the amount to top up: ")
            u.topup(amt)
        elif resp == "4":
            r = input("""Enter: 1   to search by price
                        2   to search by genre
                        3   to search by category \n""")
            if r == "1":
                app = s.searchPrice()
                if app:
                    user.buy(app)
            elif r == "2":
                app = s.searchGenre()
                if app:
                    user.buy(app)
            elif r == "3":
                app = s.searchCategory()
                if app:
                    user.buy(app)
        elif resp == "5":
            del user
            return 0
        else:
            resp = input("Invalid response, please try again.")

        


welcomePrompt = "Welcome to STIM library!"
print (welcomePrompt)
u = User(None, None, None)
l = Library()
s = Store()
selectServices()




      