import stdiomask 
import getpass


def getUsername(username):
    username = input("Username: ")
    return username

def getPassword(password):
    password = stdiomask.getpass()
    return password

def getBalance(balance): 
    balance = "0.00 php"
    print("\nBalance: ", balance)    
    return balance

def printLib(lib):
    userLib = "None"
    print("Your library: ", userLib)
    return lib        

def login():
    userData = None
    print ("Please input your username and password")
    userName = getUsername(userData)
    passWord = getPassword(userData)

    while passWord != "herbert":
        print("\nPassword is incorrect! Try Again")
        passWord = getPassword(userData)
    else:  
        print ("\nWelcome, {}!".format(userName))
    balance = getBalance(userData)
    viewLib = printLib(userData)
 
def main():
    welcomePrompt = "Welcome to Don Jose XP's Game library!"
    print (welcomePrompt, "\n")
    login()
    
if __name__ == "__main__":
    main()    







