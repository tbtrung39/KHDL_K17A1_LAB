ngày = int(input("Nhập ngày: "))
tháng = int(input("Nhập tháng: "))
năm = int(input("Nhập năm: "))
if not  1 <= ngày <= 31:
    print("Ngày không hợp lệ.")
if not  1 <= tháng <= 12:
    print("Tháng không hợp lệ.")
if  năm < 0:
    print("Năm không hợp lệ.")
ngày_trong_tháng = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ngày += 1
if ngày > ngày_trong_tháng[tháng - 1]:
    if tháng == 12:
        năm += 1
        tháng = 1
        ngày = 1
    else:
        tháng += 1
        ngày = 1
print("Ngày tiếp theo:", ngày,tháng,năm ) 