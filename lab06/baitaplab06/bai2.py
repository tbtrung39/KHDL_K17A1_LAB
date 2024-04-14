n = int(input("enter a number:"))
list1=[]
for i in range(0,n):
    number = int(input(f"Nhập phần tử thứ {i+1}:"))
    list1.append(number)
print(list1)
max_number = max(list1)
find_second_lagest = False
second_lagest = list1[0]
for i in list1:
    if i!=max_number:
        if  i>second_lagest:
            second_lagest=i
            find_second_lagest=True
if find_second_lagest:
    vitri = list1.index(second_lagest)
    print(f"the second of the lagest {second_lagest} in position {vitri+1}")
else:
    print("No")
#Tính số lượng các phần tử dương liên tiếp nhiều nhất
max_count=0
current_count =0
for i in list1:
    if i>0:
        current_count+=1
        if current_count>max_count:
            max_count=current_count
    else:
        current_count=0
print(f"the maximum number of consecutive positive number is {max_count}")
#Tính số lượng các số dương liên tiếp có tổng lớn nhất
max_sum=0
sum1=0
for i in list1:
    if i>0:
        max_sum+=i
        if sum1>max_sum:
            max_sum=sum1
    else:
        max_sum=0
print("tổng dương lớn nhất là:",max_sum)
