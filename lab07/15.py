list1 = [1,2,3,4,5,6,7,8,9]
list2 = ["T", "H", "Y", "U", "O", "P", "D", "B", "V"]
dic = {}
for i in range(len(list1)): 
    key = list1[i]
    value = list2[i]
    dic[key] = value
print(dic)