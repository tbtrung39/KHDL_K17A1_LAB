'''
Một website yêu cầu người dùng nhập tên người dùng và mật khẩu để đăng ký. Viết chương trình để kiểm tra tính hợp lệ của mật khẩu mà người dùng nhập vào. Các tiêu chí kiểm tra mật khẩu bao gồm thỏa mãn đầy đủ các yêu cầu sau:
a. Ít nhất 1 chữ cái nằm trong [a-z].
b. Ít nhất 1 số nằm trong [0-9].
c. Ít nhất 1 kí tự nắm trong [A-Z].
d. Ít nhất 1 ký tự nằm trong [$ # @].
e. Độ dài mật khẩu tối thiều: 6 ký tự.
f. Độ dài mật khẩu tối đa: 12 ký tự.
'''
def kiem_tra_mat_khau(mat_khau):
    #Đảm bảo độ dài mật khẩu từ 6 đến 12 ký tự
    if len(mat_khau) < 6 or len(mat_khau) > 12:
        return False

    #Các tập hợp ký tự đặc biệt và số
    ky_tu_dac_biet = ('$','#','@')
    so = ('0','1','2','3','4','5','6','7','8','9')

    #Biến đếm cho các loại ký tự
    co_chu_cai_thuong = False
    co_chu_cai_hoa = False
    co_so = False
    co_ky_tu_dac_biet = False

    #Kiểm tra mật khẩu
    for ky_tu in mat_khau:
        if ky_tu.islower():
            co_chu_cai_thuong = True
        elif ky_tu.isupper():
            co_chu_cai_hoa = True
        elif ky_tu in so:
            co_so = True
        elif ky_tu in ky_tu_dac_biet:
            co_ky_tu_dac_biet = True

    #Trả về True nếu mật khẩu thỏa mãn tất cả các yêu cầu
    return co_chu_cai_thuong and co_chu_cai_hoa and co_so and co_ky_tu_dac_biet

def main():
    mat_khau = input("Nhập mật khẩu: ")

    if kiem_tra_mat_khau(mat_khau):
        print("Mật khẩu hợp lệ")
    else:
        print("Mật khẩu không hợp lệ")

if __name__ == "__main__":
    main()
