# viết chương trình nhập một số và tính tổng các chữ số  của số vừa nhập rồi hiển thị kết quả nhập một số của bạn và nhập 0 để tính tổng các số vừa tính
while True:
    n = int(input("Nhập số n: "))
    if n < 0:
        break
    sum = 0
    for i in range(n):
        sum += int(input(f"Nhập số thứ {i+1}: "))
    print(f"Tổng các số vừa nhập là: {sum}")

    
    