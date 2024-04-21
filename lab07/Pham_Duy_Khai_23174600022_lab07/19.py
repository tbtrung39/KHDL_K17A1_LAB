a=[]
n=int(input('nhập số nhân viên:'))
while len(a) < n:
    ma=(input('nhập mã nhân viện gồm 4 chữ số:'))
    if len(ma)!=4:
        print('nhập lại mã nhân viên!!!')
        continue
    ten=input('nhập tên nhân viên:')
    namsinh=int(input('nhập năm sinh:'))
    luong=int(input('nhập lương:'))
    a.append({'mã':ma,
              'tên':ten,
              'năm sinh':namsinh,
              'lương':luong})
print(a)

#tìm nhân viên
x=input('nhập mã nhân viên muốn tìm:')
for i in a:
    if x==i['mã']:
            print(f'thông tin nhân viên:{i}')
            break

#tăng lương cho nhân viên
y=input('nhập mã nhân viên muốn tăng lương:')
for i in a:
    if y==i['lương']:
            (i['lương'])+=1000000
            break
  
#xóa nhân viên
z=input('nhập mã nhân viên muốn xóa:')
for i in a:
    if z==i['mã']:
        a.remove(i)
        break
else:
    print('không có nhân viên với mã nhân viên được nhập vào')
    
#sắp xếp giảm theo năm sinh
dic_new=sorted(a,key= lambda x: x['năm sinh'],reverse=True)
print(dic_new)