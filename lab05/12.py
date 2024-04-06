A = input("Nhập chuỗi A: ")
B = input("Nhập chuỗi B: ")
A_with_asterisk = ""
for char in A:
    if char.isdigit():
        A_with_asterisk += "+" + char
    else:
        A_with_asterisk += char

B_with_asterisk = ""
for char in B:
    if char.isdigit():
        B_with_asterisk += "+" + char
    else:
        B_with_asterisk += char
found_equation = False
for i in range(1, len(A_with_asterisk)):
    for j in range(1, len(B_with_asterisk)):
        C = int(A_with_asterisk[:i].replace("+", ""))
        D = int(A_with_asterisk[i:].replace("+", ""))
        E = int(B_with_asterisk[:j].replace("+", ""))
        F = int(B_with_asterisk[j:].replace("+", ""))
        if C + D == E + F:
            print(f"{C}+{D}={E}+{F}")
            found_equation = True
            break
    if found_equation:
        break

if not found_equation:
    print("Không tồn tại cách đặt!")