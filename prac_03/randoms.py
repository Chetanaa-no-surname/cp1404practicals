import random
# Line 1:
# Smallest: 5
# Largest: 20
print(random.randint(5, 20))

# Line 2:
# Smallest:3
# Largest: 9
# This cannot produce a 4 since with the skip, the possible numbers will
# only be [3,5,7,9]. There will be no even numbers like 4
print(random.randrange(3, 10, 2))

# Line 3
# Smallest: 2.5
# Largest: 5.5
print(random.uniform(2.5, 5.5))

# Line 4:
print(random.randint(1,100))
