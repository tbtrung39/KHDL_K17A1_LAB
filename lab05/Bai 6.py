'''
Nhập một chuỗi Str từ bàn phím, kiểm tra chuỗi Str có phải là chuỗi được viết trong hệ
Hex (0,1....,9, A, B,C,D,E,F) hay không. 
Nếu không phải thì loại bỏ các ký tự không thuộc hệ Hex và chuyên chuỗi còn lại sang số thập phân.
'''
def la_chuoi_hex(chuoi):
    #Tạo một set chứa tất cả các ký tự hợp lệ trong hệ Hex
    hex_chars = set("0123456789ABCDEF")

    #Kiểm tra từng ký tự trong chuỗi
    for char in chuoi:
        #Nếu ký tự không thuộc hệ Hex, trả về False
        if char.upper() not in hex_chars:
            return False
    #Nếu tất cả các ký tự đều thuộc hệ Hex, trả về True
    return True

def loai_bo_ky_tu_khong_hop_le(chuoi):
    #Tạo một chuỗi mới chỉ chứa các ký tự hợp lệ trong hệ Hex
    hex_chars = "0123456789ABCDEF"
    ky_tu_hop_le = [char for char in chuoi if char.upper() in hex_chars]
    return ''.join(ky_tu_hop_le)

def hex_sang_thap_phan(chuoi):
    #Chuyển đổi chuỗi hệ Hex sang số thập phân
    return int(chuoi, 16)

#Nhập chuỗi từ bàn phím
chuoi = input("Nhập chuỗi: ")

#Kiểm tra xem chuỗi có phải là chuỗi Hex không
if la_chuoi_hex(chuoi):
    print("Chuỗi là chuỗi Hex.")
else:
    print("Chuỗi không phải là chuỗi Hex.")

    #Loại bỏ các ký tự không phải Hex và chuyển chuỗi còn lại sang số thập phân
    chuoi_hex = loai_bo_ky_tu_khong_hop_le(chuoi)
    print("Chuỗi sau khi loại bỏ các ký tự không hợp lệ:", chuoi_hex)
    
    #Chuyển đổi chuỗi Hex thành số thập phân
    so_thap_phan = hex_sang_thap_phan(chuoi_hex)
    print("Số thập phân tương ứng:", so_thap_phan)
