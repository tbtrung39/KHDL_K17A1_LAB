so_to_chu = {'0': 'không', '1': 'một', '2': 'hai', '3': 'ba', '4': 'bốn', '5': 'năm', '6': 'sáu', '7': 'bảy', '8': 'tám', '9': 'chín'}
so = input("Nhập một số thập phân: ")
so_chu = ""
for chu_so in so:
    so_chu += so_to_chu[chu_so] + " "
print("Số", so, "được viết bằng chữ là:", so_chu)