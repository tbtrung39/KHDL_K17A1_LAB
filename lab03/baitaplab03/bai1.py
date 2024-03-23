n = int(input("Nhập vào n:"))
t1=1
result=1
for i in range(0,n+1):
    t1*=(2*(i+1))/(2*i+3)
    result+=t1
print(f"Tổng  chuỗi là {result}")