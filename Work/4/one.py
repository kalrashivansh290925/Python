# Random number

import random
# # ran_int = random.randint(1,10)
# print(ran_int)
# # Note: Random module is a python module.

# import my_module
# print(my_module.my_fav_pi)
 
random_number_0_to_1 = random.random()
print(random_number_0_to_1)
# Used to create the random number, 0.0 <= X < 1.0

random_float = random.uniform(1, 10)
print(random_float)
# random.uniform(a, b) inclusive of a and b

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads", random_heads_or_tails)
else:
    print("Tails")