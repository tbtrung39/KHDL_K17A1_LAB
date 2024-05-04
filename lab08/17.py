from functools import reduce

def tinh_tong_chan(danh_sach):
    tong_chan = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, danh_sach), 0)
    return tong_chan

def nhap_danh_sach():
    try:
        n = int(input("Nhập vào số nguyên n: "))
        danh_sach = list(range(1, n+1))
        return danh_sach
    except ValueError:
        print("Vui lòng nhập một số nguyên.")

def main():
    danh_sach = nhap_danh_sach()
    if danh_sach:
        tong_chan = tinh_tong_chan(danh_sach)
        print("Tổng các số chẵn từ 1 đến", danh_sach[-1], "là:", tong_chan)

if __name__ == "__main__":
    main()
