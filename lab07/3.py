# nhap n
import  random
n=int(input("moi nhap so n"))
# sinh mot tap hop a
numbers=[random.uniform(0,100) for _ in range(n)]
# phan tu lon nhat
max_numbers=max(numbers)
# pt nho nhat
min_number=min(numbers)
# tong
sum_numbers=sum(numbers)
# in ra 
print(max_numbers)
print(min_number)
print(sum_numbers)