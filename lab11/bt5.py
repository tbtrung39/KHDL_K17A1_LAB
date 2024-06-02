sbd_ph_path = 'lab11/Sbd_Ph.dat'
sbd_ten_path = 'lab11/SBD_Ten.txt'
phieu_diem_path = 'lab11/Phieu_Diem.txt'
ketqua_path = 'lab11/Ketqua.txt'
sbd_ph_data = {}
sbd_ten_data = {}
phieu_diem_data = {}
with open(sbd_ph_path,'r') as file:
    for line in file:
        sbd, phach = line.split()
        sbd_ph_data[int(phach)] = int(sbd)

with open(sbd_ten_path,'r') as file:
    for line in file:
        sbd, ten = line.split(maxsplit=1)
        sbd_ten_data[int(sbd)] = ten.strip()

with open(phieu_diem_path,'r') as file:
    for line in file:
        phach, diem = line.split()
        phieu_diem_data[int(phach)] = float(diem)
result = []
for phach, sbd in sbd_ph_data.items():
    if phach in phieu_diem_data:
        diem = phieu_diem_data[phach]
        ten = sbd_ten_data.get(sbd, 'Unknown')
        result.append((sbd, ten, diem))
result.sort(key=lambda x: x[2], reverse=True)
with open(ketqua_path, 'w', encoding='utf-8') as file:
    for sbd, ten, diem in result:
        file.write(f"{sbd} {ten} {diem:.2f}\n")
print("Kết quả đã được ghi vào tệp Ketqua.txt")