numbers = [1,2,3]
names = ["Mạnh","Gâu Gâu","Meo Meo"]
dct_a = dict()
for i in range(len(names)):
    a= {numbers[i] : names[i]}
    dct_a.update(a)
print(dct_a)