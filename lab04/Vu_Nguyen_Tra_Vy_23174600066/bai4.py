while True:
    t =  int(input('nhập vào tử số của phân số : '))
    m = int(input('nhập vào mẫu số của phân số : '))

    if t ==0 or m ==0:
        print('nhập lại số khác khoogn ')
        continue
    else:
        print('phân số của bạn vừa nhập vào là :',t,'/',m)
        break