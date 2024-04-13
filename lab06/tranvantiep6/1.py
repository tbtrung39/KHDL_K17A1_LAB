a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
# tổng các phần tử trong danh sách : 
tong = sum(a)
print(tong)
# Đếm số lượng số hạng dương và tổng các số hạng dương đó : 
sum = 0 
count = 0 
for i in a : 
    if i >0 : 
        sum += i 
        count += 1 
print(f"số lượng số dương là {count}, tổng là {sum}")
# vị  trí của phần tử âm trong danh sách : 
for j in a : 
    if j < 0 : 
        print("vị trí của phần tử âm đầu tiên trong danh sách là : ", a.index(j))
        break
# vị trí của phần tử dương cuối cùng trong danh sách : 
list_moi = []
for n in a : 
    if n > 0 : 
        list_moi.append(n)
print("vị trí của phần tử dương cuối cùng là : ", a.index(list_moi[-1]))
#Phần tử lớn nhất trong danh sách và vị trí lớn nhất cuối cùng : 
ptu_max = max(a)
vtri_max = a.index(ptu_max)
print(f"phần tử lớn nhất là {ptu_max}, vị trí của phần tử là {vtri_max}")
