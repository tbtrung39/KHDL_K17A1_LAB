#bài 10
chu_so = ['không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín']
so = int(input("Nhập một số thập phân: "))
chia_so = [int(x) for x in str(so)]
chuoi_chu_so = ''
i = 0
while i < len(chia_so):
    chuoi_chu_so += chu_so[chia_so[i]] + ' '
    i += 1
print(f"{so} là {chuoi_chu_so.strip()}")