#Viết chương trình tính diện tích xung quanh, 
#diện tích toàn phần và thể tích khối trụ với  bán kính và chiều cao nhập từ bàn phím (Làm tròn đến số thập phân thứ hai). Biết pi = 3.14

#BÀI 1
#TÍNH DIỆN TÍCH XUNH QUANH
r=int(input("nhập bán kính:"))
h=int(input("nhập chiều cao:"))
Sxq=(3.14*2*r*h)
print("diện tích xung quanh khối trụ là:",Sxq)
#TÍNH DIỆN TÍCH TOÀN PHẦN
Stp=3.14*r*(r+h)
print("diện tích toàn phần của khối trụ là:",Stp)
#TÍNH THỂ TÍCH KHỐI TRỤ
v=3.14*r**2*h
print("thể tích khối trụ là:",v)


