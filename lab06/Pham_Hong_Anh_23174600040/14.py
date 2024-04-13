# Nhập mật khẩu từ người dùng
pas = input("Nhập mật khẩu của bạn: ")

# Khởi tạo biến cờ kiểm tra các điều kiện
tm_az = False
tm_AZ = False
tm_09 = False
tm_đk = False
do_dai_hop_le = 6 <= len(pas) <= 12

# Các ký tự đặc biệt hợp lệ
ky_tu_dac_biet = {'$', '#', '@'}

# Duyệt qua từng ký tự trong mật khẩu để kiểm tra các điều kiện
for ky_tu in pas:
    if 'a' <= ky_tu <= 'z':
        tm_az = True
    if 'A' <= ky_tu <= 'Z':
        tm_AZ = True
    if '0' <= ky_tu <= '9':
        tm_09 = True
    if ky_tu in ky_tu_dac_biet:
        thoa_man_ky_tu_dac_biet = True

# Kết hợp các điều kiện để đưa ra kết quả
mat_khau_hop_le = (tm_az and tm_AZ and tm_09 and thoa_man_ky_tu_dac_biet and do_dai_hop_le)

# In kết quả
if mat_khau_hop_le:
    print("Mật khẩu hợp lệ.")
else:
    print("Mật khẩu không hợp lệ.")