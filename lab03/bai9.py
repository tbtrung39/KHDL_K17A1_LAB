n = int(input("Nhập n: "))
s4 = 0
s5 = 0
s6 = 0
for i in range(1,n+1):
    s4 += i**2
    if n <= 0:
        break
    
for j in range(1, n+1, 2):
    s5 += j**3
    if n <= 0:
        break

for k in range(0, n+1 ,2):
    s6 += k**4
    if n <= 0:
        break

print("s1= ", s4)
print("s2= ", s5)
print("s3= ", s6)