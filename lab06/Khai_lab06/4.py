a=[]
while True:
    b=int(input('nhập số:'))
    if b==0:
        break
    a.append(b)
#chèn [1,2,3]
b=a
m=[1,2,3]
b.insert(0,m)
b.insert(len(a),m)
b.insert(4,m)
print(b)
#xóa phần tử thứ k
k=int(input('nhập phần tử thứ muốn xóa:'))
a.pop(k)
print(a)
#sắp xếp tăng dần
print(f'tăng dần: {a.sort()}')
#giảm dần
print(f'giảm dần: {a[::-1]}')
