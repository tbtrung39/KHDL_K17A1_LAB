a = [2,-4,1,9,-3,6,3,-2,6,8]
#a
tong = sum(a)
print(f"tổng các phần tử là {tong}")
#b
ptduong = [i for i in a if i > 0]
print(f"số lương phần tử dương là {len(ptduong)}")
print(f"tổng các phần tử dương = {sum(ptduong)}")
#c
vtriamdt = [i for i, j in enumerate(a) if j < 0]
if vtriamdt:
    print("Vị trí của phần tử âm đầu tiên trong danh sách là:", vtriamdt[0])
#d
vtridcc = [i for i, j in enumerate(a) if j > 0]
if vtridcc:
    print("Vị trí của phần tử dương cuối cùng trong danh sách là:", vtridcc[-1])
#e
print(f"phần tử lớn nhất của list là {max(a)}")
amax = max(a)
print(f"vị trí của phần tử lớn nhất {a.index(amax)}")