password = input("Nhập mật khẩu: ")
if len(password) < 6 or len(password) > 12:
    print("Mật khẩu không hợp lệ.")
    if not any(char.islower() for char in password):
        print("Mật khẩu không hợp lệ.")
        if not any(char.isdigit() for char in password):
          print("Mật khẩu không hợp lệ.")
          if not any(char.isupper() for char in password):
               print("Mật khẩu không hợp lệ.")
               special_chars = r'[$#(a)]'
               if not any(char in special_chars for char in password):
                   print("Mật khẩu không hợp lệ.")
print("Mật khẩu họp lệ")