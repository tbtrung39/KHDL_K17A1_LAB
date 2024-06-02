def day_so(n):
    if n<2:
        return 1
    else:
        return n + day_so(n-1)
def so_binh_phuong(n):
    if n<2:
        return 1
    else:
        return n**2 + day_so(n-1)
try:
    n = int(input("nhap n: "))
    if n<1:
        raise ValueError("loi ")
except ValueError as e:
              print(e)
else:
       print(day_so(n))
       print(so_binh_phuong(n))