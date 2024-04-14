# Với n được nhập vào từ bàn phím .Hãy viết chương trình sử dụng list comprehension để in dãy Fibonanci dưới dạng được tách biệt bằng dấu ","
n = int(input("Nhập số n: "))
values = []

for i in range(n + 1):
    if i == 0:
        values.append(0)
    elif i == 1:
        values.append(1)
    else:
        values.append(values[i - 1] + values[i - 2])

print(" ".join(map(str, values)))
