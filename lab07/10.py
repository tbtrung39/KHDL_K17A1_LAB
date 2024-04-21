m = set(str(int(input("Nhập vào giá trị m:"))))
n = set(str(int(input("Nhập vào giá trị n:"))))
q = m.intersection(n) # phép giao
result = 0
for i in q:
    result = result + int(i)
   
print(result)
