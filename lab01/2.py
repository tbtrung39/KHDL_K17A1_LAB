so_giay=int(input('Nhập số giây muốn đổi :'))
ngay = so_giay // 86400
gio = (so_giay % 86400) // 3600
phut = ((so_giay % 86400) % 3600) // 60
giay = ((so_giay % 86400) % 3600) % 60
print(f"{so_giay} giây là {ngay} ngày, {gio} giờ, {phut} phút, {giay} giây.")