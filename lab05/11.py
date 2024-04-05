a ="011001100"
a_new =  a[::-1]
s=0
print(a_new)
for i in range(len(a)):
    s+=int(a_new[i]*(2**i))
print(s)