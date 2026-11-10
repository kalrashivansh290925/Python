# # Subscripting
# print("hello"[-5])


# # String
# print("123"+"888")


# # Integer = Whole number
# print(12+33)


# # Large Integers, readabilty
# print(123_454_79)


# # Float = floating point number
# print(3.14678)


# # Boolean
# print(True)


# # type checking
# s=len("1234567")
# print(type(s))


# # primitive data types
# #  int, boolean, string, char


# # type conversion
# print(int("123"))


# print("Number of letters in your name: " + str(len(input("Enter your name: "))))
# # shows error because concatenation can be done on same dtypes


# # Operators
# print(3 * 2)
# print(3/2)
# print(3//2) # removes decimal places
# print(2**2)

# # PEMDAS
# # (), **, * or /, + or -

# # BMI
# bmi = 84 / 1.65 ** 2
# print("BMI\n"+str(bmi))
# print(int(bmi))
# print(round(bmi))
# print(round(bmi,2))


# # Increment/Decrement
# score = 0
# score += 1
# print(score)


# # f-strings
# print("Your score is " + str(score))    

# score = 0
# height = 1.8
# is_winning = True
# print(f"Your score is = {score}, Your height is = {height}, You are winning = {is_winning }")


# a=int("5")/int(2.7)
# print(a)


# #Project
# print(round((150 * (1 + (12 / 100)) / 5), 4))

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percent tip would you like to give? "))
people = int(input("How many people to split the bill? "))

bill_tip = round((bill * (1 + (tip / 100)) / people), 2)
print(f"Each person should pay ${bill_tip}")
