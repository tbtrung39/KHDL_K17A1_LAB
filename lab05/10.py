
n = input("Nhập vào một chuỗi nhị phân: ")
so_thap_phan = 0
so_mu = 0

# Duyệt qua từng chữ số nhị phân từ phải sang trái
for i in range(len(n) - 1, -1, -1):
    if n[i] == "1":
        so_thap_phan += 2 ** so_mu
    so_mu += 1

print("Số thập phân chuyển từ số nhị phân ban đầu là:", so_thap_phan)