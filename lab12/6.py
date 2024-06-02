try:
    username = input("Enter Username: ")
    valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    for i in username:
        if i not in valid_chars:
            raise ValueError("Lỗi.")
except ValueError as e:
    print(e)
else:
    print(username + "@companyname.com")
