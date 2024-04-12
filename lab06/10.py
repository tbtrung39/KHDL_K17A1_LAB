import random
s = [n for n in range(0, 201) if n%5==0 and n%7==0]
so_ngau_nhien = random.choice(s)
print("So ngau nhien duoc chon la: ", so_ngau_nhien)