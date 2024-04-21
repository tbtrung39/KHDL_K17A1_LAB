n = int(input("Nhap mot so : "))
dic = {}
for i in range(1, n + 1): 
    key = i 
    value = i * i 
    dic[key] = value
print(dic)