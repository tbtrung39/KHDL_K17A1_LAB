a = [2, 3, 4, 5, 6, 7, 8, 9]
b = ["T", "Q", "Y", "H", "N", "B", "P", "G"]
dic = {}
for i in range(len(a)):
    dic[a[i]] = b[i]
print(dic)