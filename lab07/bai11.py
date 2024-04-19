c={1,2,3,4,5,6,7,8,9,10,11}
j={1,3,6,7,8}
p={1,4,3,9,10,11}
all = c & j & p
print(all )
a=(c.intersection(j).difference(p))|(c.intersection(p).difference(j))|(j.intersection(p).difference(c))
print(a)
b=(c.symmetric_difference(j).symmetric_difference(p)) - all 
print(b)