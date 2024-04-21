numbers=[]
while True:
    n=input("Nhap so tu nhien(nhan esc de ket thuc):")
    if n=="esc":
        break
    if n.isdigit():
        numbers.append(n)
a = set(numbers)
print("Tap hop A la:",a)
