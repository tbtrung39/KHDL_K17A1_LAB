n = int(input("nhập số lượng phần tử của danh sách:"))
list = []
for i in range(n):
    num = int(input(f"nhập số lượng phần tử của danh sách {i+1}:"))
    list.append(num)
if len(list) < 2:
    print("không có phần tử lớn thứ 2:")
else:
    max_num = max(list[0], list[1])
    min_num = min(list[0] , list[1])
    for i in range(2, len(list)):
        if list[i] > max_num:
            min_num = max_num
            max_num = list[i]
        if list[i] > min_num and list[i] !=  max_num:
            min_num = list[i]
    print(f"phần tử lớn thứ 2 trong danh sách{min_num}")
# tính số lượng liên tiếp nhiều nhất 
max_sum = 0 
tong_max = 0 
min_sum = 0 
tong_min = 0 
for num in list:
    if num > 0:
        tong_max += num
        tong_min += 1
        if tong_max > max_sum:
            max_sum = tong_max
            min_sum = tong_min
    else:
        tong_max = 0
        tong_min = 0 
print(f"số dương liên tiếp nhiều nhất là {max_sum}")
print(f"các số lượng liên tiếp nhiều nhất là {min_sum}")

        
    