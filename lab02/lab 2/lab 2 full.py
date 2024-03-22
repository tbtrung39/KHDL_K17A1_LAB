# câu 1
month = int(input('nhập số tháng bạn cần biết ngày ở đây :'))
year =  int(input('nhập năm của tháng bạn muốn kiểm tra : '))

if 0<month<=12 and year >0:
    if month<8 and month%2!=0:
        print('tháng ',month,'là tháng có 31 ngày ')
    elif 8<=month and month%2 == 0:
        print('tháng ',month,'là tháng có 31 ngày ')
    elif 2<month<8 and month%2 ==0:
        print('tháng ',month,'là tháng có 30 ngày ')
    elif 8< month and month %2!=0:
        print('tháng ',month,'là tháng có 30 ngày ')
    elif month ==2:
        if year %4==0 or year %400==0:
            print('do năm bạn nhâp là năm nhuận  nên tháng 2 có 29 ngày')
        else:
            print('do năm bạn nhập là năm k nhuận nên tháng 2 có 28 ngày')
else:
    print('không có tháng đó ')

# câu 2
    
import math


a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))


delta = b**2 - 4*a*c


if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Phương trình có hai nghiệm:")
    print("x1 =", x1)
    print("x2 =", x2)
elif delta == 0:
    x = -b / (2*a)
    print("Phương trình có một nghiệm kép:")
    print("x =", x)
else:
    print("Phương trình không có nghiệm thực")

# câu 3
day =  int(input('nhập ngày trong tuần ở đây nhé : '))
if 0<day <=7:
    if day ==1:
        print(day,'Sunday')
    elif day  == 2:
        print(day,'Monday')
    elif  day  ==  3:
        print(day,'Tuesday')
    elif day == 4:
        print(day,'Wednesday')
    elif day ==5:
        print(day,'Thursday')
    elif day == 6:
        print(day,'Friday')
    elif  day == 7 :
        print(day,'Saturday')
else:
    print('trong tuần k có thứ đấy ')
# CÂU 4
num =  int(input('nhập số nguyển cần xuất hàng trăm ra ở đây : '))
if num<100:
    print('0')
else:
    num2 = (num//100) % 10
    print('hàng trăm của số ',num,'là :',num2)

# câu 5
month =  int(input('nhập tháng trong năm ở đây nhé : '))
if 0<month <=12:
    if month ==1:
        print(month,'January')
    elif month  == 2:
        print(month,'February  ')
    elif  month  ==  3:
        print(month,'March')
    elif month == 4:
        print(month,'April')
    elif month ==5:
        print(month,'May')
    elif month == 6:
        print(month,'June')
    elif  month == 7 :
        print(month,'July')
    elif  month == 8 :
        print(month,'August')
    elif  month == 9 :
        print(month,'September')
    elif  month == 10 :
        print(month,'October')
    elif  month == 11 :
        print(month,'November')
    elif  month == 1 :
        print(month,'December')
else:
    print('tháng đây k có trong năm  ')

# câu 6
a=int(input('nhập số có 3 chữ số:'))
if a/100>10:
    print('nhâp số có 3 chữ số!!!!Vui lòng nhập lại')
else:
    hang_tram=a//100
    chu_tram=''
    chu_chuc=''
    chu_don_vi=''
    if hang_tram==1:
        chu_tram='một'
    elif hang_tram==2:
        chu_tram='hai'
    elif hang_tram==3:
        chu_tram='ba'
    elif hang_tram==4:
        chu_tram='bốn'
    elif hang_tram==5:
        chu_tram='năm'
    elif hang_tram==6:
        chu_tram='sáu'
    elif hang_tram==7:
        chu_tram='bảy'
    elif hang_tram==8:
        chu_tram='tám'
    elif hang_tram==9:
        chu_tram='chín'
    hang_chuc=a//10-(a//100*10)
    if hang_chuc==1:
        chu_chuc='một'
    elif hang_chuc==2:
        chu_chuc='hai'
    elif hang_chuc==3:
        chu_chuc='ba'
    elif hang_chuc==4:
        chu_chuc='bốn'
    elif hang_chuc==5:
        chu_chuc='năm'
    elif hang_chuc==6:
        chu_chuc='sáu'
    elif hang_chuc==7:
        chu_chuc='bảy'
    elif hang_chuc==8:
        chu_chuc='tám'
    elif hang_chuc==9:
        chu_chuc='chín'        
    hang_don_vi=a-a//10*10
    if hang_don_vi==1:
        chu_don_vi='một'
    elif hang_don_vi==2:
        chu_don_vi='hai'
    elif hang_don_vi==3:
        chu_don_vi='ba'
    elif hang_don_vi==4:
        chu_don_vi='bốn'
    elif hang_don_vi==5:
        chu_don_vi='năm'
    elif hang_don_vi==6:
        chu_don_vi='sáu'
    elif hang_don_vi==7:
        chu_don_vi='bảy'
    elif hang_don_vi==8:
        chu_don_vi='tám'
    elif hang_don_vi==9:
        chu_don_vi='chín' 
    if a%100==0:
        print(f'{chu_tram} trăm')
    elif a%100<=9:
        print(f'{chu_tram} trăm linh {chu_don_vi}')
    elif a%10==0:
        if a==110:
         print('một trăm mười')    
        else:
         print(f'{chu_tram} trăm {chu_chuc} mươi')
    else:
        if hang_chuc==1:
            print(f'{chu_tram} trăm mười {chu_don_vi}')
        else:    
            print(f'{chu_tram} trăm {chu_chuc} mươi {chu_don_vi}')

# câu 7
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

# câu 8
    
tnct =  int(input('nhập hệ số lương ở đây : '))
if 0<tnct :
    if tnct <12:
        const = 2.34
    elif 12<= tnct <36:
        const =3.33
    elif 36<= tnct< 60:
        const  =  3.66
    elif tnct >=60:
        const =3.99
    
else:
    print('hệ số lương k  hợp lệ ')
 

print('lương của nhân viên có hệ số lương '
      ,const,'là :',const*1350000,'đòng')

# câu 9
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

# câu 10
start=int(input('nhập giờ bắt đầu(5->22):'))
end=int(input('nhập giờ kết thúc(5->22):'))
thoi_gian=end-start 
if thoi_gian<=3:
    tien=thoi_gian*100000
else:
    tien=thoi_gian*100000*(3/4)
if 11<=start<=14 and 12<=end<=15:
    tien=tien*(9/10)
print('tiền phải trả: ',tien)

# câu 11

day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))


if month == 12:
    day_trong_month_tiep_theo = 31
else:
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
        day_trong_month_tiep_theo = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        day_trong_month_tiep_theo = 30
    else:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            day_trong_month_tiep_theo = 29
        else:
            day_trong_month_tiep_theo = 28


if day == day_trong_month_tiep_theo:
    day_moi = 1
    if month == 12:
        month_moi = 1
        year_moi = year + 1
    else:
        month_moi = month + 1
        year_moi = year
else:
    day_moi = day + 1
    month_moi = month
    year_moi = year


print('ngày tiếp theo là : ',day_moi,'/',month_moi,'/',year_moi)

