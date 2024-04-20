ds = [2,3,4,5,6,7,8,-6,-6,8,-9,-7,4,5,6,7,-5,-4,-6,3,-5]
a=sorted(ds,reverse=True)
print('số dương chuyển sang phải list là:',a)
# chèn số m vào đầu , cuối , vị trí thứ 5 ds
m= input('nhập phần tử cần chèn ở đay: ')
ds.insert(0,m)
b =len(ds)
ds.insert(b,m)
ds.insert(6,m)
print('ds sau khi chèn là:',ds)