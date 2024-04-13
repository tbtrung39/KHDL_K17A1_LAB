import random

subject = ["Anh", "Em"]
verb = ["Choi", "Yeu"]
object = ["Bong da", "Bong ro"]
for i in range(2): 
    cau = f"{random.choice(subject)} {random.choice(verb)} {random.choice(object)}"
    print(cau)
    
