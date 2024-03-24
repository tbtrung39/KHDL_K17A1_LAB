
list = {'0': 'không','1': 'một','2': 'hai','3': 'ba','4': 'bốn',
                '5': 'năm','6': 'sáu','7': 'bảy','8': 'tám', '9': 'chín'}


lua_chon =  input('nhập một số  : ')

a= ''
for i in lua_chon:
    if i in list:
        a +=list[i] + ' '


print(lua_chon,'là :',a)