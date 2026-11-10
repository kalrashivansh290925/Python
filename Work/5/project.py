import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

# print("Welcome to PyPassword Generator")
nl = int(input("How many letters? "))
nn = int(input("How many numbers? "))
ns = int(input("How many symbols? "))


# # EASY
# password = ""

# for char in range(0, nl):
#     # char = random.choice(letters)
#     char = letters[random.randint(0,25)]
#     password += char.upper() if random.randint(0, 1) else char

# for char in range(0, nn):
#     password += random.choice(numbers)

# for char in range(0, ns):
#     password += random.choice(symbols)

# print(password)


# HARD

pass_list = []

for char in range(0, nl):
    # char = random.choice(letters)
    char = letters[random.randint(0,25)]
    pass_list  += char.upper() if random.randint(0, 1) else char

for char in range(0, nn):
    pass_list  += random.choice(numbers)

for char in range(0, ns):
    pass_list  += random.choice(symbols)

print(pass_list )
random.shuffle(pass_list)
print(pass_list)

password = ""
for char in pass_list:
    password += char

print(f"Your password is: {password}")