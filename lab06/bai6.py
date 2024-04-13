import random 
a = [random.randint(1,99999) for _ in range(1000)]
a_sort = sorted(a)
print("A sau khi đc sorted; ", a_sort)

a = [random.randint(1,99999) for _ in range(1000)]
n = len(a)
for i in range(n-1):
    for j in range(0, n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j + 1] = a[j + 1] , a[j]
print("Dãy sau khi sắp xếp ko dùng sorted : ", a)