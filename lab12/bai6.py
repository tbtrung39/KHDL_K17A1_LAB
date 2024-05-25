def nhap_email(username):
    for char in username:
        if not char.isalnum():
            raise ValueError("ten nguoi chi duoc chua chu cai va chu so khong duoc chua ky tu dac biet")
    return username + "@companyname.com"

try:
    ds_email=[]
    so_email=int(input("nhap so luong email muon tao: "))
    
    
    for i in range (so_email):
        username = input("nhap username: ")
        email=nhap_email(username)
        ds_email.append(email)
        print("email vua duoc tao:", email)
    print("danh sach cac dia chi email vua luu:", ds_email)

except ValueError as e:
    print(f"loi: {e}")
except Exception as f:
    print(f"loi khong xac dinh: {f}")
