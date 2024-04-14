a=[]
while True:
    b=int(input('nhập số:'))
    if b==0:
        break
    a.append(b)
#chuyển các kí tự dương lên đầu
a.sort()
a=a[::-1]
print(a)
#chèn vào đầu, cuối, 5
m=int(input('nhập số muốn chèn:'))
a.insert(0,m)
a.insert(len(a),m)
a.insert(4,m)
print(a)


