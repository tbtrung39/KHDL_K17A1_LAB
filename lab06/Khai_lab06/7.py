List = [['mon',73],['tue',89],['wed',95],['thu',103],['fri',115],['sat',128],['sun',120]]
print('phần tử thứ 2 của list thứ 3',List[2][1])
#độ dài
print('độ dài của list là:',len(List))
# thêm một sublisst
List.insert(2,['a',1])
print(List)
# tính tổng  sale value
a =List[0][1]
b =List[1][1]
c =List[5][1]
d =List[6][1]
print('tổng sale value là: ',a+b+c+d)
