def tao_dia_chi_email(username, domain="companyname.com"):
    return f"{username}@{domain}"

def nhap_username():
    while True:
        username = input("Nhập username: ")
        if kiem_tra_username(username):
            return username
        else:
            print("Username không hợp lệ. Vui lòng nhập lại. Username chỉ bao gồm chữ cái thường, chữ cái hoa và số, không được có dấu cách.")

def kiem_tra_username(username):
    if username.isalnum():
        return True
    return False

def main():
    danh_sach_email = []
    so_luong = int(input("Nhập số lượng username cần nhập: "))
    
    for _ in range(so_luong):
        username = nhap_username()
        dia_chi_email = tao_dia_chi_email(username)
        danh_sach_email.append(dia_chi_email)
    
    print("Danh sách email:")
    for email in danh_sach_email:
        print(email)

main()
