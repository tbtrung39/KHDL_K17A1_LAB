chu_so = {'0': 'không','1': 'một','2': 'hai','3': 'ba','4': 'bốn','5': 'năm','6': 'sáu','7': 'bảy','8': 'tám','9': 'chín'}
so = input("Nhập một số thập phân : ")
i = 0
while i < len(so):
    so1 = so[i]
    print(chu_so[so1], end=' ')
    i += 1