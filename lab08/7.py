def gtln(a,b,c):
    ln = max(a,b,c)
    nn = min(a,b,c)
    return ln , nn 
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
gt = gtln(a,b,c)
print(gt)
