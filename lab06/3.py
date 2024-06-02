list=[]
while True:
    number=int(input("Nhập giá trị (Nhập 0 để dừng):"))
    if number==0:
        break
    list.append(number)
print("Danh sách trong list:",list)
ds_sap_xep=sorted(list,reverse=True)
print("Danh sách được sap xếp:",ds_sap_xep)
new_number=int(input("Nhập giá trị mới:"))
list.insert(0,new_number)
list.insert(4,new_number)
list.append(new_number)
print("danh sach mới:",list)