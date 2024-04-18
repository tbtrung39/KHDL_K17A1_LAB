A = (input("NHap mot chuoi so thuc : "))
A = set(A)
mn = min(A)
mx = max(A)
sum = 0 
for i in A : 
    sum += int(i)
print(mn, mx, sum)
