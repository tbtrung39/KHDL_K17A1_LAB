Numbers=[]
while True:
    char=input('Nhập các số tự nhiên (Bấm ENTER để kết thúc):')
    if char == '':
        break
    Numbers.append(int(char))
A=set(Numbers)
print('Tập hợp A gồm những phần tử vừa nhập là :',A)
    