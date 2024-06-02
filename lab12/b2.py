def kiem_tra_ky_tu(chuoi):
    for char in chuoi:
        if not char.isalpha():
            return False
    return True

def kiem_tra_chuoi_lien_tiep(chuoi, do_dai):
    for i in range(len(chuoi) - do_dai + 1):
        if chuoi[i:i+do_dai] == chuoi[i]*do_dai:
            return True
    return False

def nhap_chuoi():
    while True:
        try:
            chuoi = input("Nhập một chuỗi ký tự: ")

            if not kiem_tra_ky_tu(chuoi):
                raise ValueError("Lỗi ký tự !!!")
            elif kiem_tra_chuoi_lien_tiep(chuoi, 2):
                raise ValueError("Lỗi nhập liệu !!!")
            elif kiem_tra_chuoi_lien_tiep(chuoi, 4):
                raise ValueError("Lỗi nhập lặp lại !!!")
            elif kiem_tra_chuoi_lien_tiep(chuoi, 5):
                raise ValueError("Lỗi nhập trùng lặp !!!")
            else:
                print("Chuỗi đã nhập:", chuoi)
                break

        except ValueError as ve:
            print("Lỗi:", ve)

nhap_chuoi()
