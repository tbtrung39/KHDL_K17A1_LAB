so_thanh_chu = {'0': 'không', '1': 'một', '2': 'hai', '3': 'ba', '4': 'bốn', '5': 'năm', '6': 'sáu', '7': 'bảy', '8': 'tám', '9': 'chín'}
so = input("Nhập một số: ")
kq = ""
vi_tri = 0
while vi_tri < len(so):
    chu_so = so[vi_tri]
    kq+= so_thanh_chu[chu_so] + " "
    vi_tri += 1
print("Số", so, "được viết bằng chữ là:",kq)