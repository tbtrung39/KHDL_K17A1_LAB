list=[]
while True :
    n=int(input("nhập số tự nhiên :"))
    list.append(n)
    if n == 0:
        break
list.sort(reverse=True)
print("danh sách sau khi đã chuyển đổi là :" ,list)
m=input("Nhập m từ bàn phím ")
list.insert(0,m)
list.insert(-1,m)
list.insert(5,m)
print(list)
