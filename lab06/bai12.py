D = int(input("nhập số  lần  gửi đầu vào: "))
W = int(input("nhập vào số lần rút tiền: "))
listd = []
listw = []
for i in range(D):
    d = int(input(f"nhập vào số tiền lần gửi thứ {i + 1}: "))
    listd.append(d)
for j in range(W):
    w = int(input(f"nhập vào số tiền lần rút thứ {i + 1}: "))
    listw.append(w)
if sum(listd) < sum(listw):
    print(f"số tiền rút đã vượt quá giới hạn không thực hiện được!")
else:
    tongmax = [max(listw),max(listd)]
    print(f"tổng giá trị lớn nhất của gửi và rút là {sum(tongmax)}")