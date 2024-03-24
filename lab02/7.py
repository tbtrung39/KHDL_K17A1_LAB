diem  =  float(input('nhập điểm cần biết học lực vào đây :  '))

if 0<=diem<=10:
    if 0<=diem<=3:
        print(diem,'là loại kém')
    elif 4<=diem<=5:
        print(diem,'là loại yếu')
    elif 5<diem<=6:
        print(diem,'là loại trung bình')
    elif 7<=diem<=8:
        print(diem,'là loại khá ')
    elif 9<=diem<=10:
        print(diem,'là loại giỏi ')
else:
    print('điểm từ 1 đến 10 thôi ạ ')