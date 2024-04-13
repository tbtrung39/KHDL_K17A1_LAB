x=int(input("nhập vào giá trị x:"))
y=int(input("nhập vào giá trị y:"))
list_cha=[]
for i in range(0,x):
    list_con=[]
    for j in range(0,y):
        list_con.append(i*j)
    list_cha.append(list_con)
print(list_cha)