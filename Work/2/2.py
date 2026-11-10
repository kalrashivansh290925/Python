# print("Welcome to the rollercoaster!")
# height = int(input("What is your height? "))

# if height >= 120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry")

# s = int(input("Enter a number"))
# if s % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")


# # lec 25

# if int(input("What is your height? ")) >= 120:
#     print("You can ride the rollercoaster!")

#     age = int(input("What is your age? "))
#     if age <= 12:
#         bill = 4
#         print("Ticket price = $4")
#     elif age <= 18:
#         bill = 7
#         print("Ticket price = $7")
#     else:
#         bill = 10
#         print("Ticket price = $10")

#     wants_photo = input("Do you want to take a photos? (y/N) ")

#     if wants_photo == "y":
#         bill += 3
        
#     print(f"Your final bill is : ${bill}")

# else:
#     print("Sorry")


# # Python pizza, lec 26
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepproni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill +=25
# else:
#     print("You have entered the wrong input.")

# if pepperoni == "Y":
#     bill += 3

# if extra_cheese == "Y":
#     print(f"The total amount is ${(bill+1)}")

# else:
#     print(f"The total amout is ${bill}")


# lec 27

print('''
              .              .
              \\            i|
    _-^-_      \`.          ||
   / .^. `.     \ \   ,///.' |
  / /   `. \     \ `-'       |
 / /      > >     \          |
< <      / /       \         |
 `.\    /,'         \        |
  //   //            `___     ^-_
 //   ||              \  ^-_--~~/
 '     ||              *`-' `*-'
        ||             ,\ _-_|
         \ .-_.,^^^.,'/ `\|||
          "/  -'      /.   \|'
          /          / |    '
         /              |
        m__----___   /_-`m
                  ^-m'
''')

print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at the crossroad. Where to go? ' \
                'Type "left" or "right".').lower()
# Backslash(\) -> Escape symbol, lower() -> used to lowercase the letters or str.

print("She said 'Hello'.")

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. ' \
                    'There is an Island in the middle of the lake. ' \
                    'Click "W" to wait for a boat. ' \
                    'Type "S" to swim across.').lower()
    if choice2 == "w":
        choice3 = input("You arrived the island unharmed. ' \
                        'There is house with 3 doors Red, Yellow, and Blue. '\
                        'Whcih color do you choose? ").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over!")
        elif choice3 == "yellow":
            print("You found treasure.")
        elif choice3 =="blue":
            print("You entered a room full of beasts. Game Over!")
            
    else:
        print("You attacked by an angry shark.")
else:
    print("You fell into a hole. Game Over!")