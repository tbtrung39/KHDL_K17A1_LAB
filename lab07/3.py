#3
A=[]
while True:
    so = input("Nhập số tự nhiên (Nhập 'xong' để kết thúc): ")
    if so == 'xong':
        break
    if so.isdigit(): 
        A.append(float(so))
    else:
        print("Vui lòng nhập số tự nhiên.")
maxA=max(A)
minA=min(A)
tongA=sum(A)
print(f"số lớn nhất tập hợp A là : ", maxA)
print(f'số nhỏ nhất tập hợp A là : ' ,minA)
print(f'tổng là A : ', tongA)
