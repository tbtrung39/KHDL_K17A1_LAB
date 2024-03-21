n = int(input("Nhập giá trị n: "))

if n <= 0:
    print("Không phải là số hoàn hảo")
else:
    print(f"Các số hoàn hảo nhỏ hơn {n}:")
    for i in range(1, n):
        sum = 0
        for j in range(1, i):
            if i % j == 0:
                sum += j
        if sum == i:
            print("số hoàn hảo còn lại và nhỏ hơn số hoàn hảo hiện tại là",i)