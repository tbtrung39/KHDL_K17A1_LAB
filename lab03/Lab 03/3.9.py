'''
Viết chương trình nhập n là số nguyên dương.
Nếu n<=0 thì dừng chương trình.
Sau đó tính các tổng sau bằng vòng lặp for:
a) S4 = 1^2 + 2^2 + 3^2 + … + n^2.
b) S5 = 1^3 + 3^3 + 5^3 + … + (2n+1)^3.
c) S6 = 2^4 + 4^4 + 6^4 + … + (2n)^4.
'''
n = int(input("nhập vào số nguyên tố n: "))
suma = 0
sumb = 0
sumc= 0
for i in range(1,n+1):
    suma += i**2
    if i % 2 == 0:
        sumb += i**3
    if i % 2 != 0:
        sumc += i**4
    if n <= 0:
        break
print(suma)
print(sumb)
print(sumc)