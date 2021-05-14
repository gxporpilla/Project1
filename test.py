from unittest import result
from user import User
from Library import Library
import unittest
import sqlite3, time

with sqlite3.connect("main.db") as db:            
    cursor = db.cursor()

class TestProgram(unittest.TestCase):
    def test_getGameData(self):
        l = Library()
        l.getGameData(220)
        self.assertEqual(l.appId, 220)
        self.assertEqual(l.gameName, 'Half-Life 2')
        self.assertEqual(l.release, '11/16/2004')
        self.assertEqual(l.developer, 'Valve')
        self.assertEqual(l.categories, 'Single-player;Steam Achievements;Steam Trading Cards;Captions available;Partial Controller Support;Steam Cloud;Includes Source SDK')
        self.assertEqual(l.genre, 'Action')
        self.assertEqual(l.tags, 'FPS;Action;Sci-fi')
        self.assertEqual(l.price, 7.19)

    def test_SuccessLogin(self):
        u = User(None, None, None)
        result = u.login('TheeeHman', 'jerusalem393')
        self.assertTrue(result)

    def test_FailLogin(self):
        u = User(None, None, None)
        result = u.login('TheeeHmaan', 'jerusalem393')
        self.assertFalse(result)

    def test_SuccessSignup(self): #Success Signup: Username is unique, "vicsloan" is the existing username in db. 
        #Meaning, this method tests whether the method has successfully concluded that the username is unique
        u = User(None, None, None)
        result = u.signUp('vicsloans', 'intel1')    
        self.assertFalse(result)

    def test_FailSignup(self): #Fail Signup: Username is already taken and already exists in db. 
        #Meaning, this method tests whether the method has successfully found the exact match username in db.
        u = User(None, None, None)
        result = u.signUp('vicsloan', 'intel1')    
        self.assertTrue(result)



if __name__=='__main__': 
    unittest.main()
        
        