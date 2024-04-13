# 
x=int(input("moi nhap x"))
y=int(input("moi nhap y"))
list_cha=[]
for i in range(0,x):
    list_con=[]
    for j in range(0,y):
        list_con.append(i*j)
    list_cha.append(list_con)
print(list_cha)