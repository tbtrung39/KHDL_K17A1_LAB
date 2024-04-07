'''
Cho trước hoặc nhập từ bàn phím chuôi ký tự Str. 
Hãy tìm một chuỗi ký tự con có độ dài cực đại và bao gồm các phần tử giống nhau của chuỗi ký tự trên. 
Ví dụ : Chuỗi ký tự nhập vào là:"aabbco" thì chuỗi ký tự in ra sẽ là : "bbb"
'''
def tim_chuoi_con_giong_nhau(str):
    max_chuoi = ""
    chuoi_hien_tai = ""
    for char in str:
        if chuoi_hien_tai == "":
            chuoi_hien_tai = char
        elif char == chuoi_hien_tai[-1]:
            chuoi_hien_tai += char
        else:
            if len(chuoi_hien_tai) > len(max_chuoi):
                max_chuoi = chuoi_hien_tai
            chuoi_hien_tai = char
    #Kiểm tra chuỗi cuối cùng
    if len(chuoi_hien_tai) > len(max_chuoi):
        max_chuoi = chuoi_hien_tai
    return max_chuoi

#Nhập chuỗi từ bàn phím
chuoi = input("Nhập chuỗi: ")

#Tìm chuỗi con có độ dài cực đại và bao gồm các phần tử giống nhau
chuoi_con_max = tim_chuoi_con_giong_nhau(chuoi)
print("Chuỗi ký tự con có độ dài cực đại và bao gồm các phần tử giống nhau:", chuoi_con_max)
