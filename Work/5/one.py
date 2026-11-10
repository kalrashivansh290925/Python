# fruits = ["Apple", "Peach", "Mango"]
# print(fruits)
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")


student_score = [143, 26, 78, 150, 21, 23,120]
total = sum(student_score)
print(total)
print(max(student_score))

maximum = 0
for score in student_score:
    if score > maximum:
        maximum = score

print(maximum)