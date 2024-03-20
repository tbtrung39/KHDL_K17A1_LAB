h = float(input("Nhập chiều cao khối trụ:"))
r = float(input("Nhập bán kính:"))
import math
dtxq = 2*math.pi*r*h
dttp = dtxq+2*math.pi*r**2
thetich = math.pi*r**2*h
print("Diện tích xung quanh %0.2f"%dtxq)
print("Diện tích toàn phần %0.2f"%dttp)
print("Thể tích là %0.2f"%thetich)