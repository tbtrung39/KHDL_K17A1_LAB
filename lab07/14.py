dic = {}
for i in range(1, 101) : 
    key = i 
    value = bin(i)[2: ]
    dic[key] = value
print(dic)