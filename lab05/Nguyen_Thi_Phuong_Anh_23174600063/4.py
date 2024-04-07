n = input("Nhap chuoi 1:")
m = input("Nhap chuoi 2:")
len1 = len(n)
len2 = len(m)
t_str = ''
i = 0
j = 0
while i < len1 or j < len2:
    if i < len1:
        t_str += n[i]
        i += 1
    if j < len2:
        t_str += m[j]
        j += 1
print("Chuoi sau khi lam tron la",t_str)
