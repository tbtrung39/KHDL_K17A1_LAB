n = int(input("Nhap so luong phan tu list: "))
list1 = []

for i in range(n):
    num = int(input('Nhap phan tu thu  {} :'.format(i+1)))
    list1.append(num)
print('Danh sach da nhap: ',list1)

#phan tu lon thu hai
so_lon_nhat = so_lon_thu_hai = float('-inf')

for num in list1:
    if num > so_lon_nhat:
        so_lon_thu_hai = so_lon_nhat
        so_lon_nhat = num
    elif num > so_lon_thu_hai and num != so_lon_nhat:
        so_lon_thu_hai = num
print('Phần tử lớn th ứ hai là: ',so_lon_thu_hai )