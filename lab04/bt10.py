a = input("Nhập 1 số: ")
i = 0
while i < len(a):
    b  =  a[i]
    if b == '1':
        print('một',end=' ')
    elif b == '2':
        print('hai',end=' ')
    elif b == '3':
        print('ba',end=' ')
    elif b == '4':
        print('bốn',end=' ')
    elif b == '5':
        print('năm',end=' ')
    elif b == '6':
        print('sáu',end=' ')
    elif b == '7':
        print('bảy',end=' ')
    elif b == '8':
        print('tám',end=' ')
    elif b == '9':
        print('chín',end=' ')
    else:
        print('không',end=' ')
    i+=1