#BÀI 2
r=float(input('nhập bán kính:'))
h=float(input('nhập chiều cao:'))
Sxq=round(2*3.14*r*h,2)
Stp=round(Sxq+2*3.14*pow(r,2),2)
V=round(pow(r,2)*3.14*h,2)
print(f'diện tích xung quanh:{Sxq}')
print(f'diện tích toàn phần:{Stp}')
print(f'thể tích:{V}')
