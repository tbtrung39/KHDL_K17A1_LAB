a=int(input("nhập số kw điện tiêu thụ:"))
if 0<=a<=100:
    tien_dien1=a*2000
    print("tiền điện là",tien_dien1)
if 101<=a<=200:
    tien_dien2=a*2500
    print("tiền điện là",tien_dien2)
if 201<=a<=300:
    tien_dien3=a*3000
    print("tiền điện là:",tien_dien3)
if a>300:
    tien_dien4=a*5000
    print("tính điện là:",tien_dien4)
    