List_ = [["mon",73],["tue",89],["wed",95],["thu",103],["fri",115],["sat",128],["sun",120]]
#in các phần tử ra màn hình
print(List_)
#chọn phần tử thứ 2 thuộc vị trí thứ 3 của sublist
print(f"phần tử thứ hai thuộc vị trí thứ 3 là: {List_[3][1]}")
#kiểm tra độ dài
print(f"độ dài list là:{len(List_)}")
#tổng sale trong các ngày thứ 2,thứ 3 , thứ 7, chủ nhật
tong = List_[0][1]+ List_[1][1] + List_[5][1] + List_[6][1]
print(f"tổng sale trong các ngày thứ 2, thứ 3, thứ 7 và chủ nhật là:{tong}")