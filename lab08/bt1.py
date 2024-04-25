def so_ke_tiep(x):
    try:
        x = int(x)
        return x + 1
    except ValueError:
        return "Vui lòng nhập một số nguyên."

so_nhap_vao = input("Nhập một số nguyên: ")
print(so_ke_tiep(so_nhap_vao))