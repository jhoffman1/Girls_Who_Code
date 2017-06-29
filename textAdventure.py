start = '''
It's pay day!
After paying your bills, you've calculated that you have $50 left to treat yourself with!
Where would you like to go shopping?
'''

stores = '''Type:
'candy' to go to the candy store,
'clothes' to go to the clothing store,
'dinner' to go to a fancy restaurant,
or 'home' to go home and save the rest of your money for another time!

At any time, type 'exit' to quit the adventure.
'''


money = 50

def leave():
    print("Bye!")
    exit()

def lineBreak():
    print("\n")
    print("-------------------------")

def storesDecision():
    store = input()
    lineBreak()
    if store == "candy":
        print("Who needs to wait for Halloween to indulge in some sweets?")
        candyShop()
    elif store == "clothes":
        print("Time to re-vamp the wardrobe!")
    elif store == "dinner":
        print("Call up your friends! It's dinner time!")
    elif store == "home":
        print("So responsible! Put on your favorite sweatpants and put on some Netflix.")
        print ("You have $%d left to for another time!") % money
        exit()
    elif store == "exit":
        leave()
    else:
        print("Please choose one of the previously stated options!")
        storesDecision();

def candyShop():
    print('''Pricing at this store is $2 per pound of candy.
How many pounds would you like to purchase?''')
    pounds = checkInput()

    cost = 2*pounds
    if money > cost:
        money = money - cost
        print("You purchased %d pounds of candy!") %pounds
        moneyLeft()
    else:
        print("You don't have enough money to buy that!")


#def clothingStore():


#def dinner():



def moneyLeft():
    print ("You have $%d left!")% money

def checkInput():
    user_input = input()
    if (isinstance(user_input, int) or isinstance(user_input, float)):
        return user_input
    elif user_input == "exit":
        leave()
    else:
        print("Please enter a valid number")
        checkInput();


print(start)
print(stores)

storesDecision();
