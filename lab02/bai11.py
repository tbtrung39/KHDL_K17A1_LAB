m = int(input("nhập vào ngày cho trước: "))
n = int(input("Nhập vào tháng: "))
if n <= 12 and n >=1:
    if n == 4 or n == 6 or n == 9 or n == 11:
        if m >= 1 and m <= 30:
            l = m + 1
            if l == 31:
                print("ngày mùng 1")
            else:
                print(f"ngày sau ngày cho trước là ngày {l}")
        else:
            print("không tồn tại ngày")
    elif n == 2:
        if m >= 1 and m <= 28:
            l = m + 1
            if l == 29:
                print("ngày mùng 1")
            else:
                print(f"ngày sau ngày cho trước là ngày {l}")
        else:
            print("không tồn tại ngày")
    else:
        if m >= 1 and m <= 31:
            l = m + 1
            if l == 32:
                print("ngày mùng 1")
            else:
                print(f"ngày sau ngày cho trước là ngày {l}")
        else:
            print("không tồn tại ngày này")
else:
    print("không tồn tại tháng")