a = [1,20,31,4,5]
dict = {}
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j] + 1 == a[j]:
            dict[i] = j
print(dict)