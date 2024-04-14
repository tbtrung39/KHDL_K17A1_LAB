list1=[]
while True:
    num = int(input("enter a number:"))
    if num == 0:
        break
    list1.append(num)
a = [1,2,3]
list1.insert(0,a)
list1.append(a)
if len(list1)>=5:
    list1.insert(4,a)
else:
    print("Danh sách không đủ phần từ để chèn")
print(list1)
#Xóa phần tử thứ k trong bàn phím
k = int(input("Nhập vị trí thứ k để xóa:"))
if k <1 and k>len(list1):
    print("Invalid location")
else:
    del list1[k-1]
print(list1)
#Sắp xếp danh sách theo thứ tự tăng dân giảm dần
list1.sort()
print("ascending order:",list1)
list1.sort(reverse=True)
print("descending order:",list1)

    
    
    