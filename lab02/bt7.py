Diem_TK=float(input('Nhập điểm: '))
if 0<=Diem_TK<=3:
    print('Loại kém')
elif 4<=Diem_TK<5:
    print('Loại yếu')
elif 5<=Diem_TK<=6:
    print('Loại trung bình')
elif 7<=Diem_TK<=8:
    print('Loại khá')
elif 9<=Diem_TK<=10:
    print('Loại giỏi')
else:
    print('Không có trong thang điểm')