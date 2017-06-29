print("Welcome to the Mall!")
print("You can go into Sephora, Forever 21, or adidas!")
print("You have $100 to spend.")
print("Which store do you want to go into?")

choosingStore = True
storeChoice = ""
money = 100

while choosingStore == True:
    storeChoice = input()
    
    if (storeChoice == "Sephora"):
        choosingStore = False
        print("Welcome to Sephora!")
        print("You can buy Urban Decay eyeliner for $50 or Matte LipStick for $35")
        print("To purchase eyeliner, type 'e'. To purchase the Lipstick, type 'l'.")        

        sephoraChoice = input()
        if (sephoraChoice == 'e') :
            print("Great choice! That eyeliner is poppin'")
            money = money - 50
            print ("You have $%d left" %(money))
        elif (sephoraChoice == 'l'):
            print("That color looks great on you!")
            money = money - 35
        
    elif (storeChoice == "Forever 21"):
        choosingStore = False

    elif (storeChoice == "adidas"):
        choosingStore = False
    else:
        print("Please type one of the above options")
