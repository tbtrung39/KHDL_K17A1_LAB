'''
Viết chương trình tạo danh sách Numbers các phần tử là số tự nhiên nhập từ bàn phím 
và sinh một tập hợp A với các phần tử thuộc danh sách Numbers.
'''
Numbers=[]
while True:
    char=input('Nhập các số tự nhiên (Bấm ENTER để kết thúc):')
    if char == '':
        break
    Numbers.append(int(char))
A=set(Numbers)
print('Tập hợp A gồm những phần tử vừa nhập là :',A)