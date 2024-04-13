list = [2,3,4,5,6,7,-2,-4,-6,-8,-9,8,4,7,-7]
a = sorted(list,reverse=True)
print("Số dương chuyển sang phải danh sách là:",a)

# chèn số m vào đầu , cuối, vị trí t5 list
m = input("Nhập phần tử cần chèn ở đây:")
list.insert(0,m)
b = len(list)
list.insert(b,m)
list.insert(6,0)
print("Danh sách sau khi chèn là:",list)
