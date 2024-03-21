import math
a = int(input("nhập điểm a:"))
b = int(input("nhập điểm b:"))
c = int(input("nhập điểm c:"))
delta = b**2 - 4*a*c  
a != 0
if delta < 0:
    print("phương trình có vô nghiệm")
elif delta == 0: 
    x = -b/2*a 
    print("phương trinh có nghiệm kép", x)
elif delta > 0 :
    x1 = (-b + math.sqrt(delta))/2*a
    x2 = (-b - math.sqrt(delta))/2*a
    print("nghiệm của phương trình 1 là ", x1)
    print("nghiệm của phương trình 2 là", x2)