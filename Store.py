class Store:
    
    print("Welcome, User", "\n")

def displayGames(): 
    Yes = "Y"
    yes = "y"
    next = Yes
    count = 10
    while next is Yes or yes:
        count1 = (count-10)
        c.execute("SELECT rowid, NAME, TAGS FROM GAMES WHERE rowid BETWEEN ? and ?", (count1,count))
        items=c.fetchall()
        for item in items:
            print(item)

        next = input("Next page? [y/n]")
        if next is Yes or yes:
            count += 10
        else:
            break
            break
    displayGames()

    def displayPrices():
        print("Display all prices?")
        answer=input ("y/n = ")
        if answer=="y":
            print ("100")
            print ("200")
            print ("300") 
            print ("400")
        elif answer=="n":
            return displayGames()
        else:
            print("Enter valid choice")
            return displayPrices()
            while displayPrices()!="n":
                return displayPrices()
        
    displayPrices()