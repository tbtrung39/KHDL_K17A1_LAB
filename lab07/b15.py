numbers = [1,2,3]
names = ["Vinh","Khanh","NauNau"]
dct_a = dict()
for i in range(len(names)):
    a= {numbers[i] : names[i]}
    dct_a.update(a)
print(dct_a)