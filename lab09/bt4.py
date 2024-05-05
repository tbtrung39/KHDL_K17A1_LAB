def hoan_vi(danh_sach):
    if len(danh_sach) == 1:  # Nếu chỉ có một phần tử trong danh sách
        return [danh_sach]   # Trả về danh sách này

    hoan_vis = []  # Tạo một danh sách rỗng để lưu trữ các hoán vị
    for i in range(len(danh_sach)):  # Duyệt qua từng phần tử trong danh sách
        dau_tien = danh_sach[i]  # Chọn một phần tử làm phần tử đầu tiên của hoán vị
        con_lai = danh_sach[:i] + danh_sach[i+1:]  # Loại bỏ phần tử đã chọn khỏi danh sách còn lại

        for hoan_vi_con_lai in hoan_vi(con_lai):
            hoan_vis.append([dau_tien] + hoan_vi_con_lai)  # Thêm hoán vị vào danh sách

    return hoan_vis  # Trả về danh sách các hoán vị

n = int(input("Nhập một số tự nhiên n: "))

danh_sach = list(range(1, n+1))

for hoan_vi in hoan_vi(danh_sach):
    print(hoan_vi)
