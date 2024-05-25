while True:
    try:
        s = input("Nhập chuỗi ký tự: ")
        if not s.isalpha():
            raise ValueError('lỗi ký tự')
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                raise ValueError('lỗi nhập dữ liệu')
        for i in range(len(s) - 3):
            if s[i] == s[i + 1] == s[i + 2] == s[i + 3]:
                raise ValueError('lỗi nhập lập lại')
        words = s.split()
        for i in range(len(words) - 4):
            if words[i] == words[i + 1] == words[i + 2] == words[i + 3] == words[i + 4]:
                raise ValueError('lỗi nhập trùng lặp')
        print(f"Bạn đã nhập: {s}")
    except ValueError as e:
        print(e)
