doan_van="tu don chinh là tu chi co mot am tiet, hoac mot tieng cau tao thanh"
kiem_tra=input("nhap vao mot tu don: ")
if kiem_tra.isalpha() and kiem_tra == kiem_tra.replace(" ",""):
    print("Co",doan_van.count(kiem_tra),"tu` :",kiem_tra)
else:
    print(kiem_tra,"khong phai la tu don")