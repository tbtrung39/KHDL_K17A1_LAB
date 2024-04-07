Str=input('Nhap chuoi ky tu:')
num_str=''
for char in Str:
    if char.isdigit():
        num_str+=char
print('Chuoi so khi loai bo cac ky tu khong phai so:',num_str)
if num_str.isdigit():
    num = int(num_str)
    tong_uoc=0
    for i in range(1,num):
        if num % i == 0:
            tong_uoc+=i
    if tong_uoc==num:
        print('la chuoi hoan hao')
    else:
        print('khong la chuooi hoan hao')
else:
    print('khong phai chuoi so')