'''
Cho chuỗi ký tự Strl. Ta gọi một từ trong chuôi là một dãy ký tự liên tiếp
 (không có ký tự trắng và dấu phầy) các từ này được phân cách bởi các ký tự trắng hoặc dấu phầy.
Vi dụ: Strl = "Khoa, khoa hoc ung dung" gôm các từ: "Khoa", "khoa", "học", "ứng", "dụng".
Hãy viêt chương trình in ra các từ trong chuôi Str1, môi từ in trên một dòng.
'''
def in_cac_tu(str):
    tu = str.split(", ")
    for tu_khoang_trang in tu:
        for tu in tu_khoang_trang.split(" "):
            print(tu)

Str1 = "Khoa, khoa học ứng dụng"
in_cac_tu(Str1)
