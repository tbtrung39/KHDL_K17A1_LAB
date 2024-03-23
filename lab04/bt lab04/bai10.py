
libary = {'0': 'khong','1': 'một','2': 'hai','3': 'ba','4': 'bón',
                '5': 'năm','6': 'sáu','7': 'bảy','8': 'tám', '9': 'chín'}


number =  input('nhập một số  : ')

a= ''
for i in number:
    if i in libary:
        a+=libary[i] + ' '


print(number,'là :',a)