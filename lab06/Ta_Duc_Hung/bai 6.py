import random
list=[]
for i in range(1001):
    so_ngau_nhien=random.randint(1,3)
    list.append(so_ngau_nhien)
print(list)
# xắp bằng cách sử dụng hàm sort
a=list.sorted(reversed=False)
print("xắp xếp theo thứ tự tăng dần sử dụng hàm sorted :",a)
# xắp xếp không sử dụng hàm sort
b=list[::-1]
print("xắp xếp không dùng sort là :",b)

