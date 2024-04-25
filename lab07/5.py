import random
set_a = [1,2,3,4,5,6,7,8,9]
set_b = set()
while len(set_b)<5:
    set_b.add(random.choice(set_a))
print(set_b)