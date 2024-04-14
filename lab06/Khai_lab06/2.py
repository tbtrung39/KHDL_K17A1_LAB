n=int(input('nhập số phần tử muốn nhập:'))
list=[]
for i in range(0,n):
    a=int(input('nhập số tự nhiên:'))
    list.append(a)
#tim phần tử lớn thứ hai của list
a=max(list)
t=True
while t==True:
    a-=1
    for i in list:
        if i==a:
            print(f'phần tử lớn thứ 2 của danh sách có giá trị: {i}')
            print(f'vị trí của phần tử lớn thứ 2 cảu danh sách: {list.index(i)}')
            t=False
            break

#tính số lượng các số dương liên tiếp nhiều nhất
test1=[]
test2=[]
t=0
while True:
    for i in range(0,len(list)):
        if list[i]>0:
            if len(test1)==0 or t==1:
                test1.append(i)
            else:
                test2.append(i)
        else:
            if len(test2)>len(test1):
                test2=test1
                test1=[]
                t==1
                
            
            break
        

    


