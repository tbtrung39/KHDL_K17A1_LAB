t = float(input('Thời gian sử dụng bóng đèn là(giây):'))
u = 220
i = 2.7
A = u*i*t
print("Công tiêu thụ là:",A,"(ws)")
tien = (A/3600000)*7000
print("Số tiền phải trả là:",tien,"(đồng)")
