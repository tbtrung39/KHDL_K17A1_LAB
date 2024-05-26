import md4
a=int(input(" nhap a : "))
b=int(input(" nhap b : "))
c=int(input(" nhap c : "))
print(f"{a} x X + {b} = 0")
print(f"x co gia tri bang :",md4.phuongtrinhbacnhat1an(a,b))
print(f"{a} x X^2 +{b} x X + {c} = 0")
print(md4.phuongtrinhbac2(a,b,c))