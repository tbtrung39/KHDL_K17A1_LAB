list1=[]
while True:
    num = int(input("Enter  a number:"))
    if num == 0:
        break
    list1.append(num)
    
        
positive_number = []
bin = []
for i in list1:
    if i > 0:
        positive_number.append(i) 
    else:
        bin.append(i)
positive_number.extend(bin)
print(positive_number)    
m = int(input("Nhập số m cần chèn: "))
list1.insert(0, m)
list1.append(m)
if len(list1) >= 5:
    list1.insert(4, m)
else:
    print("Danh sách không đủ 5 phần tử để chèn vào vị trí thứ 5.")
print("Danh sách sau khi chèn số m:")
print(list1)
    