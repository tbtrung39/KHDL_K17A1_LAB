while True:
    n = int(input("Nhập 1 số bất kì: "))
    if n > 0:
        break
    else:
        print("Nhập lại")
print("Số được nhập là", n)