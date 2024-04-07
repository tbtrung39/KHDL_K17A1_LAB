str = input("Nhap mot chuoi ky tu : ")
result = 0 
for i in str :
    if i.isnumeric() :
        result = result * 10 + int(i)
print(result)

#tim so hoan hao : so hoan hao la so có tong uoc so cong lai thi bang chinh no :
tong = 1
for j in range(2, result):
    if result % j == 0 :
        tong += j
if tong == result :
    print(f"{result}l la so hoan hao")
else:
    print(f"{result} khong la so hoan hao")