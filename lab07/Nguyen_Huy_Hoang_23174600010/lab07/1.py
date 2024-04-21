import keyboard as k
set=set()
while True:
    a=input('nhập số nguyên(nhấn ESC để ngừng nhập):')
    if k.is_pressed('ESC'):   #nhấn tổ hợp phím ESC + ENTER để dừng
        print('đã dừng chương trình')
        break
    # a = k.read_event(suppress=False).name          #chỉ cần ấn ESC
    # if a == "esc":
    #     break
    set.add(a)
print({x for x in set if not(str(x).isnumeric())})

