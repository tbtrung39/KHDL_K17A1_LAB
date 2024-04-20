# tao danh sach numbers
numbers=[]
# nhap phan tu va kiem tra
while True:
    phan_tu=input("moi nhap phan tu:")
    if phan_tu.lower()=="q":
        break
    if phan_tu.isdigit():
        numbers.append(int(phan_tu))
    else:
        print("vui long nhap so")
a=set(numbers)
print(a) 
