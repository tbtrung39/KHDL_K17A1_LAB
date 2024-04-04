a="011001110"
a_new=a[::-1]
s=0
for j in range(len(a)):
    s+= int(a_new[j])*(2**j)
print(s)