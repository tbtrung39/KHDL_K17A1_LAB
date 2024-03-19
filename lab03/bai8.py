n = int(input("nhập vào số nguyên tố n: "))
suma = 0
sumb = 0
sumc= 0
for i in range(1,n+1):
    if n <= 0:
        break
    suma += i
    if i % 2 == 0:
        sumb += i
    else:
        sumc += i
print(suma)
print(sumb)
print(sumc)