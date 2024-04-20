n=int(input("Nhập vào chuỗi:"))
m=list(n)
l=set(list(m))
h=dict
for i in l:
    a=m.count(i)
    b={i:a}
    d=h.update(b)
    print("Số lần K trong W:",d)