list_=[['mon',73],['tue',89],['wed',95],['thu',103],['fri',115],['sat',128],['sun',120]]
print(list_)
#chọn ra phần tử thứ hai thuộc vị trí thứ 3
print(list_[2][1])

#kiểm tra độ dài list 
print('Độ dài list:',len(list_))
# tính tổng sale value
a= list_[0][1]
b= list_[1][1]
c= list_[5][1]
d= list_[6][1]
tong= a+b+c+d
print('Tổng sale value là:',tong)
# thêm một sublist
list_.insert(3,['hp',99])
print(list_)