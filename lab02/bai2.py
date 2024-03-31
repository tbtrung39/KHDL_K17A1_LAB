a= int(input("nhập giá trị của a : "))
b= int(input("nhập giá trị của b : "))
c= int(input("nhập giá trị của c : "))
delta=(b**2)-(4*a*c)
if delta > 0:
    x1=((-b)+delta**0.5)/(a*2)
    x2=((-b)-delta**0.5)/(a*2)
    print(f"pt có 2 nghiệm x1={x1}, x2={x2}")
elif delta ==0:
    x3=(-b)/2*a
    print(f"pt có 1 nghiệm duy nhất x={x3}")
elif delta <0 :
    print("Phương trình vô nghiệm ")