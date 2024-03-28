while True:
    ky_tu = input("Nhap ky tu: ")
    if ky_tu != chr(27):
        print(f"    Ma ASCII cua ky tu {ky_tu} la {ord(ky_tu)}")
    else:
        break