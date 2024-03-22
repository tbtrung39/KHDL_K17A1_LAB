chu_so = {'0': 'không',
          '1': 'một',
          '2': 'hai',
          '3': 'ba',
          '4': 'bốn',
          '5': 'năm',
          '6': 'sáu',
          '7': 'bảy',
          '8': 'tám',
          '9': 'chín'}
n = input("Nhập số: ")
so = ''
i = 0
while i < len(so):
    n += chu_so[so[i]] + ''
    i += 1
print(f"Số {so} bằng chữ là:", n.strip())
    