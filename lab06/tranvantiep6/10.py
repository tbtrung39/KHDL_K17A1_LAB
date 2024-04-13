import random 

list_random = [random.randint(0, 200) for i in range(201)]
list_cprhs = [i for i in list_random if i % 5 == 0 and i % 7 == 0]
print(list_cprhs)