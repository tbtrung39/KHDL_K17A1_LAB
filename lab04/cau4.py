while True:
    tu_so = int(input("Nhap vao tu so la: "))
    mau_so = int(input("Nhap vo mau so la: "))
    if mau_so != 0:
        break
    else:
        print("Mau so khong duoc bang 0. Vui long nhap lai")
print("Phan so ban da nhap la: ", tu_so, "/", mau_so)