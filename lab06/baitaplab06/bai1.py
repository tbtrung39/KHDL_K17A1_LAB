a = [2,-4,1,9,-3,6,3,-2,6,8]
#Viết chương trình tính tổng các phần tử trong danh sách
sum=0
for i in a:
    sum+=i
print(sum)
#Viết chương trình đếm số lượng số các số dương và tính tổng
count=0 
sum=0
for i in a:
    if i>0:
        count+=1
        sum+=i
print("number of positive number in the list:",count)
print("sumary of positive number in the list:",sum)
#find the position number the first negative number
find_negative_number = False
for i in range(len(a)):
    if a[i]<0:
        print("the positive of the first negative number:",i)
        find_negative_number = True
        break
if not find_negative_number:
    print("there are no negative number in the list:")
#find the last positive number in the list
find_positive = False
last_positive = -1
for i in range(len(a)-1,-1,-1):
    if a[i]>0:
        last_positive=i
        find_positive = True
        break
if find_positive:
    print("the last number position in the list:",last_positive)
else:
    print("NO Positive number") 
#find the lagest number in the list and the position of the lagest number in the list
max_num = a[0]
max_position = 0
for i in range(len(a)):
    if a[i]>max_num:
        max_num=a[i]
        max_position=i
print("số lớn nhất trong danh sách là:",max_num)
print("Vị trí của số lớn nhất là:",max_position)
        

    