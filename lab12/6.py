import re

def is_valid_username(username):
    return re.match("^[a-zA-Z0-9]+$", username)

email_list = []
while True:
    username = input("Nhập tên username (hoặc 'exit' để thoát): ")
    if username.lower() == 'exit':
        break
    if is_valid_username(username):
        email_list.append(f"{username}@companyname.com")
    else:
        print("Username không hợp lệ. Vui lòng thử lại.")

print("Danh sách email nhân viên:", email_list)