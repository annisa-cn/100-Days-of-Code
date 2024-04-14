import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#code below this line 👇

rps = [rock, paper, scissors]

user_rps = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

#we're checking user's input first as we need to check the validity and generate the input as image hence it become the first condition out of the flow.
#since computer_rps is restricive to 0,1,2 (line 45), we only do the checking for user's input.

if user_rps >= 3 or user_rps < 0:
    print("You typed an invalid number, you lose!")
else:
    print(rps[user_rps])
    #the above code is used to print the ASCII art instead of inputted number

    computer_rps = random.randint(0, 2)
    print(f"Computer chose:\n {rps[computer_rps]}")

    if user_rps == 0 and computer_rps == 2:
        print("You win!")
    elif computer_rps == 0 and user_rps == 2:
        print("You lose")
    elif computer_rps > user_rps:
        print("You lose!")
    elif user_rps > computer_rps:
        print("You win!")
    elif computer_rps == user_rps:
        print("It's a draw!")
