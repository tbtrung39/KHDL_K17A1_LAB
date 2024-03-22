#câu 2
a = int(input("nhập vào giá trị a:"))
b = int(input("nhập vào giá trị b:"))
c = int(input("nhập vào giá trị c:"))
delta = b**2 - 4*a*c
if delta < 0:
    print("phương trình vô nghiệm")
if delta > 0:
    x1 = (-b + delta**0.5)/2*a
    x2 = (-b - delta**0.5)/2*a
    print(f"phương trình có hai nghiệm phân biệt {round(x1,2)} và {round(x2,2)}")
if delta == 0:
    x = -b/2*a
    print(f"phương trình có nghiệm kép:{round(x,2)}") 