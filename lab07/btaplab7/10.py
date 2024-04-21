m=set(str(int(input("Nhap vao gia trị m:"))))
n=set(str(int(input("Nhap vao gia trị n:"))))
q=m.intersection(n) 
result =0
for i in q:
    result = result + int(i)

print(result)
