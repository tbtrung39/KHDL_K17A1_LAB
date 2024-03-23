so = int(input("Nhập số là:"))
S = 1
s = 1
for i in range (0,so+1):
    s = s*((2*i)+2)/((2*i)+3)
    S = S+s
S = round(S,3)
print(S)