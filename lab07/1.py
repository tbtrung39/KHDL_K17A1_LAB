a = set()
while True:
    n=input("Nhap ki tu(nham phim Esc de ket thuc):")
    if n =="esc":
        break
    a.add(n)
a -= {n for n in a if n.isdigit()}
print("Tap hop la:",a)