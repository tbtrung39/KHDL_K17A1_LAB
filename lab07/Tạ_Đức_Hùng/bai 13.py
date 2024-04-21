W = [1, 2, 4, 6, 5, 4, 8, 3, 2, 1, 9, 5, 4]
dic = {}
for i in W : 
    key = int(i)
    value = W.count(i)
    dic[key] = value
print(dic)