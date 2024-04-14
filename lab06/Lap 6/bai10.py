import random
ags = [char for char in range(0,201) if char %5==0 and char%7==0 ]
A = random.choice(ags)
print(A)