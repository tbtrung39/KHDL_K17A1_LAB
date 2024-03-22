check_digit = input("Nhập mã số kiểm tra: ")
values = {
    'A': 10, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19,
    'J': 20, 'K': 21, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29,
    'S': 30, 'T': 31, 'U': 32, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38
}
S = 0
sum=0
for i in range(len(check_digit[:4])):
        S = values[check_digit[i]]
        sum +=S*(2**i)
for i in range(len(check_digit[4:])):
        A=int(check_digit[i+4])
        sum+=A*(2**(i+4))

so_kiem_tra=sum%11
print(f"vay so kiem tra cua ma container {check_digit} la:",so_kiem_tra)