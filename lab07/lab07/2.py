Numbers = [] 
while True:
    n=input("nhập 1 số tự nhiên (nhập enter đẻ dừng):")
    if n=='':
        break
    if n.isdigit():
        Numbers.append(int(n))
    else:
        print("vui lòng nhập lại")
A=set(Numbers)
print("danh sách các chữ số",Numbers)
print("tập hợp A",A)