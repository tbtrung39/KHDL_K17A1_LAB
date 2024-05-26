from pk6 import doicoso2

input_string = input("Nhập một chuỗi ký tự: ")
filtered_string = doicoso2.loai_bo_ky_tu_khong_hop_le(input_string)
doicoso2.kieu_co_so(filtered_string)

base = int(input("Nhập cơ số của chuỗi số bạn muốn chuyển sang cơ số 10 (2, 8, 16): "))
input_number = input("Nhập chuỗi số cần chuyển đổi: ")
doicoso2.chuyen_co_so_to_10(input_number, base)
