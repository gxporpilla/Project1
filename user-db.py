import stdiomask 
import getpass

class User: 

    with sqlite3.connect("main db.db") as db:
        cursor = db.cursor()

    def __init__(self, username, password, balance):
        self.username = username 
        self.password = password
        self.balance = balance
        
    def getUsername(self, username):
        return '{}'.format(self.username)

    def getPassword(self, password):
        return '{}'.format(self.password)

    def getBalance(self, balance): 
        return '{}'.format(self.balance)

    cursor.execute("SELECT * FROM ACCOUNTS")
    print(cursor.fetchall())    

    






