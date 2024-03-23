tu_dien_so = {
    '0': 'không', '1': 'một', '2': 'hai', '3': 'ba', '4': 'bốn',
    '5': 'năm', '6': 'sáu', '7': 'bảy', '8': 'tám', '9': 'chín'
}
while True:
    b = input("Nhập một số là: ")
    print("Kết quả in ra màn hình là:", end=" ")
    for i in b:
        print(tu_dien_so[i], end=" ")
    break