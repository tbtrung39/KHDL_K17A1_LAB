# viết chương trình nhập vào tử số và mẫu số  của 1 phân số ,kiểm tra mẫu số nếu là số 0 thì nhập lại
n = int(input("nhập tử số:"))
m = int(input("nhập mẫu số:"))
if m ==  0:
    print("vui lòng nhập lại")
else:
    while True:
        phan_so = n/m
        print("phân số của tử và mẫu là", phan_so)
        break