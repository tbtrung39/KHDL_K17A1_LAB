#bài 11
print("vui lòng chọn thức uống:")
menu = ["cafe","cam vắt","nước ép cà rốt","nước lọc","nước dừa"]
for i in enumerate (menu,1):
    print(i)
menu = ["cafe","cam vắt","nước ép cà rốt","nước lọc","nước dừa"]
while True:
    choose = int(input("which one you wanna order?:"))
    new_choose = choose - 1
    if choose == "1":
        print("bạn muốn chọn cà phê?")
    elif choose == "2":
        print("bạn muốn chọn nước cam vắt?")
    elif choose == "3":
        print("bạn muốn chọn nước ép cà rốt?")
    elif choose == "4":
        print("bạn muốn chọn nước lọc?")
    elif choose == "5":
        print("bạn muốn chọn nước dừa?")
    xac_nhan = input(f"bạn muốn chọn {menu[new_choose]}(y/n)?:")
    if xac_nhan == "y":
        print(f"thức uống bạn chọn là {menu[new_choose]}, vui lòng thay toán trước khi nhận đồ uống")
        break
    