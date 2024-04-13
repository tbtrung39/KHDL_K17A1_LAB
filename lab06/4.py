danh_sach=[]
while True:
   n=int(input("nhap so tu nhien :"))
   if n<=0:
      break
   danh_sach.append(n)
   print("Danh sach sau khi nhap:",danh_sach)
#chen phan tu vao danh sach
danh_sach.append([1,2,3])
print("danh sach sau khi chen them phan tu:",danh_sach)
danh_sach.insert(0,[1,2,3])
print(danh_sach)
danh_sach.append(4,[1,2,3])   
print(danh_sach) 
#xoa phan tu khoi danh sach
k=int(input("nhap vi tri phan tu can xoa"))  
danh_sach.pop(k)
print("danh sach sau khi xoa:",danh_sach)