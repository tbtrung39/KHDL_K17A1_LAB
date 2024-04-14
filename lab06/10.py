#Yeu cau1: su dung module random va list comprehension 
#Yeu cau 2: De xuat so ngau nhien chia het cho 5,7 trong [1,200]
import random
so=random.choice([x for x in range (1,201) if x%5==0 and x%7==0])
print("So duoc de xuat chia het cho 5,7 trong khoang[1,200] la: ",so)