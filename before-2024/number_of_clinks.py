# 2 people - 1 clink
# 3 people - 3 clinks
# 4 people - 6 clinks
# 5 people - 10 clinks
# 6 people - 15 clinks
# 7 people - 21 clinks

# How many clinks between n people

import math

def number_of_clinks(people_size):
    # It's a combination:
    # 1. Order doesn't matter (human1 clinks with human2)
    
    r = 2 # only 2 people clinks
    C = math.factorial(people_size) / (math.factorial(r) * math.factorial(people_size-r))
    
    return C

print(number_of_clinks(7))