lst=[['mom',73],['tue',89],['wed',95],['thu',93],['fri',115],['sat',128],['sun',120]]
for i in range(0,len(lst)):
    print(lst[i])
lst
print(lst[2][1])
print("da dai cua list la: ",len(lst))
lst.append(['new',100])
print("danh sach da them sublist",lst)
list_sale_value=lst[0][1]+lst[1][1]+lst[5][1]+lst[6][1]
print("tong sale value la:", list_sale_value)