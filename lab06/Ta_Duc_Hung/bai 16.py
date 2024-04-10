x=int(input())
y=int(input())
list_char=[]
for i in range(0,x):
    list_con=[]
    for j in range(0,y):
        list_con.append(i*j)
    list_char.append(list_con)

print(list_char)

