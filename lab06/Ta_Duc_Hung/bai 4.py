list=[]
while True:
    n=int(input("Nhập vào số tự nhiên n(nhập 0 để dừng lại ) :"))
    list.append(n)
    if n ==0 :
        break
print(list)
# chèn [1,2,3] vào vị trí đầu ,cuối và thứ 5 của list 
list.insert(0,1)
list.insert(4,2)
list.insert(-1,3)
# xóa phần tử thứ k nhập vòa 
k=int(input("nhập vào k "))
list.remove(list[k])
print(list)
# tạo list đảo ngược và xắp xếp theo thứ tự tăng dần giảm dần 
list.sort(reverse=False)
print("list sắp xếp theo tăng dần :",list)
list.sort(reverse=True)
print("xắp xếp list theo thứ tự giảm dần " ,list)


