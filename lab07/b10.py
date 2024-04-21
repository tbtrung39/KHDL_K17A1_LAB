m = input("nhap so tu nhen m: ")
n = input("nhap so tu nhen n: ")
m=set(m)
n=set(n)
chu_so_chung= m&n
S= list(chu_so_chung)
tong = 0
for i in S:
    tong += int(i)

print("tong cac chu so chung cua m va n la: ",tong)