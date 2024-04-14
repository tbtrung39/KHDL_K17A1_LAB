import random


random_numbers = [x for x in range(201) if x % 5 == 0 and x % 7 == 0]


random_number = random.choice(random_numbers)


print("number random dividesible for 5 and 7 about 0 to 200 ", random_number)
