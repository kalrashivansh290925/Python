states_of_america = ["Colaba", "Delaware", "Pennysylvania",""]
print(states_of_america[3])
print(states_of_america[-2])
# On seeing [] somwhere in python, we may know that this is somewhere related to lists

states_of_america[-2] = "Norway"
print(states_of_america[-2])

states_of_america.append("Rome")
print(states_of_america)

states_of_america.extend(["India", "Pak"])
print(states_of_america)

states_of_america.insert(4, "Oman")
print(states_of_america)

states_of_america.remove("")
states_of_america.pop(5)
print(states_of_america)
print(states_of_america)