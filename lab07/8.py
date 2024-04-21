n=int(input("nhập số lượng phàn tử : "))
A=set()
b=0
c=0
d=0
for i in range(n):
    phantu=input("nhập phần tử cho A : ")
    A.add(phantu)
    if phantu.isdigit():
        b+=1
    elif "." in phantu and all(char.isdigit() or char == "." for char in phantu):
        c+=1
    else:
        d+=1
print('số nguyên : ', b)
print("số thức : ", c)
print(" chuỗi kí tự : ", d)