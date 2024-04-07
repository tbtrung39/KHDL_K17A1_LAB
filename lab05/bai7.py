Str = input("Nhập chuỗi ký tự: ")
kiemtrakytu = ''.join(char for char in Str if char.isdigit())
if kiemtrakytu.isdigit():
    num = int(kiemtrakytu)
    tong = sum(i for i in range(1, num) if num % i == 0)
    if tong == num:
        print("Chuỗi số này là số hoàn hảo:", kiemtrakytu)
    else:
        print("Chuỗi số này không phải là số hoàn hảo:", kiemtrakytu)
else:
    print("Chuỗi nhập vào không phải là một số.")
