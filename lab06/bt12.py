# Nhập nhật ký giao dịch từ người dùng
nhật_ký = []
while True:
    giao_dịch = input("Nhập giao dịch (D hoặc W, số tiền) hoặc nhấn Enter để kết thúc: ")
    if not giao_dịch:
        break
    nhật_ký.append(giao_dịch)

# Tính số tiền thực của tài khoản
số_tiền_thực = 0
for giao_dịch in nhật_ký:
    loại, số_tiền = giao_dịch.split()
    if loại == 'D':
        số_tiền_thực += int(số_tiền)
    elif loại == 'W':
        số_tiền_thực -= int(số_tiền)

# In số tiền thực của tài khoản
print("Số tiền thực của tài khoản là:", số_tiền_thực)
