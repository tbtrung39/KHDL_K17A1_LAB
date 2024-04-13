x=int(input("nhap vao x: "))
y=int(input("nhap vao y: "))
lst_cha=[]
for i in range (0,x):
    lst_con=[]
    for j in range (0,y):
        lst_con.append(i*j)
    lst_cha.append(lst_con)
print(lst_cha)