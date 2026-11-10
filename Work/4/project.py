print('''  
    _______
---'  ____ )
     (_____)
     (_____)
     (____)
---.__(___)

      ___
---' _____)_____
         _______)
         _______)
        _______)
---.__________)

    _____
---' ____)____
         ______)
      __________)
     (____)
---.__(___)\n''') 
import random
print("Welcome to the game of Rock Paper and Scissors\n")
piece = input("Type 1 for rock, 2 for paper, 3 for scissor: ")

list = ["rock", "paper", "scissors"]
element = random.choice(list)
select = list.index(element)+1

print(f"The computer chose {element}")

if piece == "1":
    print("You chose rock\n")

    if select == piece:
        print("It's a draw")

    elif select == 2 :
        print("You lose!")

    else: 
        print("You won!")


elif piece == "2":
    print("You chose paper\n")

    if select == piece:
        print("It's a draw")

    elif select == 3:
        print("You lose!")

    else: 
        print("You won!")

elif piece == "3":
    print("You chose scissors\n")
    if select == piece:
            print("It's a draw")
    
    elif select == 1:
        print("You lose!")
    
    else: 
        print("You won!")
    
else: 
    print("Entered wrong input")
