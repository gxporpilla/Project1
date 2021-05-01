class Store:
    
    print("Welcome, User", "\n")

    def displayGames():
        print("Display all games?")
        answer=input ("y/n = ")
        if answer=="y":
            print ("Tekken")
            print ("Genshin")
            print ("Dota") 
            print ("LoL")
        elif answer=="n":
            exit()
        else:
            print("Enter valid choice")
            return displayGames()
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