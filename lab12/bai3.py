import os

try:
    file_path = input("nhap duong dan tap tin: ")
    if not os.path.isfile(file_path):
        raise FileNotFoundError("loi!!! tap tin khong ton tai")
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    with open('copy.dat', 'w', encoding='utf-8') as copy_file:
        copy_file.write(content)
    print("noi dung da duoc luu.")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(f"Loi: {e}")

