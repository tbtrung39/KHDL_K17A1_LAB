
m = int(input("Nhập số tự nhiên m: "))
n = int(input("Nhập số tự nhiên n: "))

str_m = str(m)
str_n = str(n)

dig_m = set(str_m)
dig_n = set(str_n)

common_digits = dig_m.intersection(dig_n)
total = sum(int(digit) for digit in common_digits)

print("Tổng các chữ số chung của m và n là:", total)
