lisst = [["mom", 73], ["tue", 89], ["wed", 95], ["thu", 103], ["fri", 115], ["sat", 128], ["sun", 120]]
print(lisst)
# chon phan tu thu hai, thuoc vi tri thu 3 cua sublist
ptu_2 = lisst[3][1]
print(ptu_2)
# kiem tra do dai cua list test va them mot sublist ngau nhien : 
length = len(lisst)
import random 

if len(lisst) >= 5 : 
    sublisst = random.sample(lisst, 5) 
else: 
    print("list khong dap ung du yeu cau !!!")
print("do dai cua list la : ", length)
print("sublisst ngau nhien la : ", sublisst)  
# tinh tong danh so ban hang trong ngay 2, 3, 7, cn ; 
list_new = [lisst[0][1], lisst[1][1], lisst[5][1], lisst[6][1]]
sum = 0 
for i in list_new: 
    sum += i 
print("tong cua sale value trong 2,3,7,cn la : ", sum )