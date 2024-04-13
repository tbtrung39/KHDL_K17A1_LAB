list=[["mon",73],["tue",89],["wed",95],["thu",103],["fri",115],["sat",128],["sun",120]]
print(list)
print("Phần tử thứ 2 thược vị trí 3:",list[2][1])
print("Độ dài của list:",len(list))
sublist=["all",429]
list.extend([sublist])
print(list)
new_list=[list[0][1],list[1][1],list[5][1],list[6][1]]
print(new_list)
print("tổng sale value:",sum(new_list))