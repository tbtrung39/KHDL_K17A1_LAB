#1
m=set()
while True:
    kt=input("nhập giá trị muốn thêm ( nhấm 'ESC' để thoát): ")
    if kt=="ESC":
        print("Kết thúc nhập")
        break
    if kt.isdigit():
            print("Ký tự số được bỏ qua.")
    else:
            m.add(kt)
    print(m)