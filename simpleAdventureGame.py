print("It's Halloween and your friends decide to explore Haunted House.")
print("Do you want to join them? (y/n)")

choice1 = input()
if (choice1 == 'y'):
    print("I like your sense of adventure! Let's go!")
elif (choice1 == 'n'):
    print("That's okay, it's not illegal to be a scaredy-cat")
    exit()
else:
    print("That wasn't one of the choices, so I'll assume that's a yes!")

print("At any time, you can type 'leave' to exit the house.")
print("You enter the haunted house and look around.")
print("There's a living room to your left and a dining room to your right.")
print("Which direction would you like to go in? (left/right")

choice2 = input()

if (choice2 == 'leave'):
    print("You leave the house still alive!")
    exit()
elif (choice2 == 'left'):
    print("You enter the living room and see an old piano.")
    print("Would you like to play a song? y/n")
    choice3 = input()
elif (choice2 == 'right'):
    print("You enter the dining room and see a staircase.")
    print("Would you like to go upstairs?")
