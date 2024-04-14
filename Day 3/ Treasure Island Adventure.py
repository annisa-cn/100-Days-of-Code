#you can find your own ASCII Art on https://ascii.co.uk/art

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

#Using three single quotes signifies that we're creating a multiline string, especially relevant when incorporating ASCII art into Python code.

#To make it more attractive, we're going to add some opening messages

print("Welcome to the mysterious shores of Treasure Island")
print("Your mission is to find the treasure.")

#The flow will go like this:
#There will be 3 stages to find the treasure.
#For the first part, player needs to choose between 'left' or 'right'.
#If the player choose right then it's game over, otherwise game will continue.
#When player pass the first stage, he/she needs to pass a lake either by swimming or by waiting for a boat.
#If the player choose to swim, then it's game over, otherwise game will continue.
#For the last stage, player needs to choose a color.
#To win the game, player needs to choose yellow, else the game will be over.
#We can access the flowchart using the link below.

#https://viewer.diagrams.net/index.html?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D

answer1 = input(
    'You\'re at a cross road. Which path will you choose? Type "left" or "right".\n'
).lower()

if answer1 == "left":
    answer2 = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n'
    ).lower()
    if answer2 == "wait":
        answer = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n"
        ).lower()
        if answer == "red":
            print("You enter a room of beasts. Game Over.")
        elif answer == "yellow":
            print("You found the treasure! You Win!")
        elif answer == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into an abyss. Game Over.")

#We utilize the .lower() method to standardize all responses, ensuring the program functions regardless of how the player enters input (e.g., LEFT, Left, or left).
