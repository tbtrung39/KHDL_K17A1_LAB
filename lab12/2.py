def check_dau_vao(input):
    if not input.isalpha():
        raise ValueError("Lỗi ký tự !!!")

    for i in range(len(input) - 1):
        if input[i] == input[i + 1]:
            raise ValueError("Lỗi nhập liệu !!!")

    for i in range(len(input) - 3):
        if input[i] == input[i + 1] == input[i + 2] == input[i + 3]:
            raise ValueError("Lỗi nhập lặp lại !!!")

    ki_tu = input.split()
    for i in range(len(ki_tu) - 4):
        if ki_tu[i] == ki_tu[i + 1] == ki_tu[i + 2] == ki_tu[i + 3] == ki_tu[i + 4]:
            raise ValueError("Lỗi nhập trùng lặp!!!")

while True:
    try:
        nhap = input("Nhập chuỗi ký tự: ")
        check_dau_vao(nhap)
        print(f"Chuỗi hợp lệ: {nhap}")
    except ValueError as ve:
        print(f"{ve}")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")