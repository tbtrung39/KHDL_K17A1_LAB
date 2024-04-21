a = set()
while True:
    n=input("Nhap ki tu(nhan esc de ket thuc):")
    if n=="esc":
        break
    if not n.isdigit():
        a.add(n)
print("Tap hop la:",a)
