import random 
A=set()
ki_tu=list("qưertyuioasdfghjklzxcvbnm123456789")
for i in range(5):
  char=random.choice(ki_tu)
  A.add(char)
  print("A:",A)
B=set()
for i in range(5):
  char=random.choice(ki_tu)
  B.add(char)
  print("B:",B)
print("cac phan tu chung cua A va B:",A&B)