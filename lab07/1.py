ky_tu = set()
print("Nhap cac ki tu vs esc de ket thuc:")
while True:
    ki_tu = input()
    if ki_tu == "":
        break
    ky_tu.add(ky_tu) if not ki_tu.isdigit() else None
print("set sau khi loai bo so la: ",)