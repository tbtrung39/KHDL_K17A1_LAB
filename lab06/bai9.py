if __name__ == "__main__":
    danh_sach = [int(x) for x in input("Nhập danh sách các số, cách nhau bởi dấu cách: ").split()]
    for so in danh_sach:
        assert so % 2 == 0, f"Số {so} không phải là số chẵn."
    print("Tất cả các số trong danh sách đều là số chẵn.")
