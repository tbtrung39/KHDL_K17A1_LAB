list=[]
while True:
    number=int(input("Nhập giá trị (Nhập 0 để dừng):"))
    if number==0:
        break
    list.append(number)
print("Danh sách trong list:",list)
chen=[1,2,3]
list.insert(0,chen)
list.insert(4,chen)
list.append(chen)
print("danh sach sau khi them:",list)
k=int(input("Nhập giá trị phải xóa:"))
for i in range(len(list)):
    if list[i]==k:
        for j in range(1,len(list)-1):
            list[j]=list[j+1]
            break
print("Trước khi xóa:",list)
list=list[:len(list)-1]
print("danh sách sau khi xóa:",list)
ds_giam_dan=sorted(list,reverse=True)
print("danh sáhc sắp xếp:",ds_giam_dan)