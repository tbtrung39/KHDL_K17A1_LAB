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
