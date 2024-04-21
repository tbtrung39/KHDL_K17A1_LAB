m = set(str(int(input('Nhap vao gia tri m :'))))
n = set(str(int(input('Nhap vao gia tri n :'))))
q = m.intersection(n)                             #PHÉP GIAO
result = 0
for i in q:
    result = result + int(i)
print(result)

