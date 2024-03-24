kwh =  float(input('nhập số KW sử dụng ở đây : '))
if kwh >0:
    if 0<kwh<=100:
        tien_dien =  kwh *2000
    elif 101<=kwh<=200:
        tien_dien =  (kwh-100)*2500 +100*2000
    elif 201<=kwh<=300:
        tien_dien = (kwh-200)*3000 +100*(2000+2500)
    elif 300<kwh:
        tien_dien = (kwh-300)*5000 + 100*(2000+2500+3000)
else:
    print('số kw không hợp lệ ')

print('số tiền điện đã sử dụng là : ',tien_dien,'đồng')