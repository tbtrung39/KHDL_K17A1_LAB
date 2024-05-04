def nam_nhuan(nam):
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        return True
    else:
        return False

def so_ngay_toi_da(thang, nam):
    if thang == 2:
        if nam_nhuan(nam):
            return 29
        else:
            return 28
    elif thang in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def main():
    nam = int(input("Nhập năm: "))
    thang = int(input("Nhập tháng (từ 1 đến 12): "))
    
    if nam_nhuan(nam):
        print(nam, "là năm nhuận.")
    else:
        print(nam, "không phải là năm nhuận.")
    
    print("Số ngày tối đa của tháng", thang, "trong năm", nam, "là:", so_ngay_toi_da(thang, nam))

if __name__ == "__main__":
    main()