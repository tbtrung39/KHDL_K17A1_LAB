list1 = [["mon",73],["tue",89],["wed",95],["thu",103],["fri",115],["sat",128],["sun",120]]
#Tạo danh sách list1 và in các phần tử của list1 ra màn hình
for i in list1:
    print(i)
#chọn ra phần tử thứ hai , thuộc vị trí thứ 3 của sublist
for sublist in list1:
    if len(sublist) > 2:  
        print(sublist[2])
    else:
        print("Sublist không đủ phần tử.")
#kiểm tra độ dài list test và thêm một sublish ngẫu nhiên
import random
if len(list1) > 0:
    random_sublist = [random.randint(0, 9) for i in range(random.randint(1, 5))]  
    list1.append(random_sublist)
    print("Đã thêm một sublist ngẫu nhiên vào list test.")
else:
    print("List test hiện đang trống.")        
print(list1)
#thực hiện tính toán tổng sale value trong các ngày thứ hai , thứ ba , thứ bảy , chủ nhật
days_of_interest = ["mon", "tue", "sat", "sun"]
total_sales = 0
for sublist in list1:
    if sublist[0] in days_of_interest:
        total_sales += sublist[1]
print("Tổng sale value trong các ngày thứ hai, thứ ba, thứ bảy và chủ nhật là:", total_sales)