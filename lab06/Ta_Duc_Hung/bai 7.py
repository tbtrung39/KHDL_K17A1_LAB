# bài 7
# tạo danh sách List_ và in ra các phần tử 
List_=[["mon",77],["tue",89],["wed",95],["thu",103],["fri",115],["sat",128],["sun",120]]
print("các phần tử của list là ",List_)
# chon ra phần tử thứ 2 , thuộc vị trí thứ 3 của sublist
print("phần tử thứ 2 thuộc vị trí thứ 3 của sublisst là :",list[2][1])
# kiểm tra độ dài của List_   và thêm một sublist ngẫu nhiên 
print("độ dài của List_ là :",len(List_))
import random
nn=random.randint()
list=[]
list.append(nn)
List_.append(list)
print("thêm 1 sublisst ngẫu nhiên vào List_ ",List_)
# tính tổng value 
a=List_[2][1]+List_[5][1]+List_[6][1]
print("tính tổng sale Value trong thứ 3 , thứ 7 và chủ nhật là : ",a)
