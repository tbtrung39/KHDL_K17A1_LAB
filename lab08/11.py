def result():
    hoten = input("Nhập tên:")
    diemtoan = float(input("Nhập điểm toán:"))
    diemly = float(input("Nhập điểm lý:"))
    diemhoa = float(input("Nhập điểm hóa:"))
    diemtrungbinh = (diemtoan+diemly+diemhoa)/3
    return [hoten,diemtoan,diemly,diemhoa,diemtrungbinh]
print(result())