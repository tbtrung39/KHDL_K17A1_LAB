x = int(input('Nhap vao x:'))
y = int(input('Nhap vao y:'))
list_cha=[]
for i in range(0,x):
    list__con=[]
    for j in range(0,y):
        list__con.append(i*j)
    list_cha.append(list__con)
print(list_cha)


#cach khac
x = int(input('Nhap vao x:'))
y = int(input('Nhap vao y:'))
list_cha=[[i*j for j in range(0,y)] for i in range(0,x)]
print(list_cha)