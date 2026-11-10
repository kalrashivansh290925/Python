# import random
# friends = ["Alice", "Bob", "Charlie", "David", "Harry"]
# # 1
# print(random.choice(friends))
# # 2
# print(friends[random.randint(0,4)])

# states = [
#     "Alabama", "Alaska", "Arizona", "Arkansas", "California",
#     "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
#     "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
#     "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
#     "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
#     "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
#     "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
#     "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
#     "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
#     "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
# ]

# print(states[50]) 
# Shows error, obviously because of indexing

# The we read nested list
country = ["India", "China", "Nepal"]
country.append("Brazil")
# country[] = "Pakistan"
# nest_list = [states, country]
# print(nest_list)
country += "Pakistan"
print(len(country))
print(country)