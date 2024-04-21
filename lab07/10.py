#10
m=set(str(int(input("nhap vao gia tri  m : "))))
n=set(str(int(input("nhap vao gia tri  n : "))))
q=m.intersection(n)
result=0
for i in q:
    result=result+int(i)
print(result)