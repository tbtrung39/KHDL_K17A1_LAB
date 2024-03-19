result = 1.0
n = int(input("nhập vào số n: "))
for n in range(1, 100):
    gtri = 1.0 
    for i in range(1, n + 1):
        gtri *= (2 * i) / (2 * i + 1)
    result += gtri
    if gtri < 0.001: 
        break
print("Kết quả:", round(result, 3))