'''
Cho trước xâu Str là một đoạn văn bản hoàn chỉnh (có thể bao gồm nhiều dòng). 
Nhập vào một từ đơn, hãy tìm trong chuỗi ký tự Str xem chứa bao nhiêu từ đơn này
'''
def dem_so_lan_xuat_hien(text, tu):
    #Chia đoạn văn bản thành các từ riêng biệt bằng cách sử dụng phương thức split()
    tu_van_ban = text.split()
    
    #Đếm số lần xuất hiện của từ trong danh sách các từ
    dem = 0
    for t in tu_van_ban:
        if t == tu:
            dem += 1
            
    return dem

#Đoạn văn bản đầu vào
van_ban = """
Python là một ngôn ngữ lập trình thông dịch, cao cấp và đa mục đích. Triết lý thiết kế của Python nhấn mạnh vào tính đọc hiểu mã thông qua việc sử dụng thụt lề đáng chú ý. Cấu trúc ngôn ngữ và phương pháp hướng đối tượng của nó nhằm mục đích giúp các lập trình viên viết mã rõ ràng, logic cho các dự án quy mô nhỏ và lớn.
"""

#Từ cần tìm số lần xuất hiện
tu_can_tim = input("Nhập từ cần tìm: ")

#Tìm số lần xuất hiện của từ trong đoạn văn bản
so_lan_xuat_hien = dem_so_lan_xuat_hien(van_ban, tu_can_tim)
print(f"Từ '{tu_can_tim}' xuất hiện {so_lan_xuat_hien} lần trong đoạn văn bản.")
