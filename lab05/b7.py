van_ban = input("Nhap mot doan van ban hoan chinh la:")
tu_don = input("Nhap vao mot tu don la:")
dem = 0
do = 0
while True:
    do = van_ban.find(tu_don,do)
    if do == -1:
        break
    dem += 1
    do += 1
print("So lan tu",tu_don,"xuat hien trong",van_ban,"la:",dem)
