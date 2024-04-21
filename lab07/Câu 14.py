'''
Tạo một từ điển chứa các số từ 1 đến 100 và chuỗi nhị phân giá trị tương ứng của các số đó 
(từ điển các cặp (1, '1'), (2, '10°), (3, '11'),...).
'''
tu_dien_nhi_phan = {}

for so in range(1, 101):
    tu_dien_nhi_phan[so] = bin(so)[2:]

for so, chuoi_nhị_phan in tu_dien_nhi_phan.items():
    print(f"{so}: {chuoi_nhị_phan}")
