sbd_ph_path = 'BAI5/Sbd_Ph.dat'
sbd_ten_path = 'BAI5/SBD_Ten.txt'
phieu_diem_path = 'BAI5/Phieu_Diem.txt'
ketqua_path = 'BAI5/Ketqua.txt'
sbd_ph_data = {}
sbd_ten_data = {}
phieu_diem_data = {}
try:
    with open(sbd_ph_path, 'r', encoding='utf-8') as file:
        for line in file:
            sbd, phach = line.split()
            sbd_ph_data[int(phach)] = int(sbd)
    
    with open(sbd_ten_path, 'r', encoding='utf-8') as file:
        for line in file:
            sbd, ten = line.split(maxsplit=1)
            sbd_ten_data[int(sbd)] = ten.strip()
    
    with open(phieu_diem_path, 'r', encoding='utf-8') as file:
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
except FileNotFoundError as e:
    print(f"File not found: {e}")
except Exception as e:
    print(f"An error occurred: {e}")