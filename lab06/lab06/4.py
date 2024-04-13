arr = []
while True:
    num = int(input("Nhập số tự nhiên (nhập 0 để kết thúc): "))
    if num == 0:
        break
    arr.append(num)
arr1=[1,2,3]
arr=arr1+arr
arr+=arr1
arr.insert(4,arr1)
print("Danh sách sau khi chèn [1, 2, 3]:",arr)
k = int(input("Nhập số k (phần tử cần xóa): "))
if 0 < k <= len(arr):
    phan_tu_xoa=arr.pop(k-1)
    print("đã xóa phần tử:",phan_tu_xoa)
else:
    print("Không có phần tử thứ", k)
print("danh sau sau khi xóa:",arr)
sắp_xếp_tăng_dần = sorted(arr)
sắp_xếp_giảm_dần = sorted(arr, reverse=True)
print("Danh sách sau khi sắp xếp theo thứ tự tăng dần:",sắp_xếp_tăng_dần)
print("Danh sách sau khi sắp xếp theo thứ tự giảm dần:",sắp_xếp_giảm_dần)
