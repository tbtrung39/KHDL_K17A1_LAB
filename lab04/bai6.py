#bài 6
a = ["một","hai","ba","bốn","năm","sáu","bảy","tám","chín","mười"]
while True:
    chon = int(input("số nhập vào:"))
    chon = chon - 1
    print(a[chon])
    nhap_tiep = input("bạn có muốn nhập tiếp không?(y/n):")
    if nhap_tiep == "n":
        break
