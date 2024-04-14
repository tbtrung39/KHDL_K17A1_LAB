list=[2,-4,1,9,-3,6,3,-2,6,8]
print(f'tổng các phần tử của list: {sum(list)})')
      
print(f'số các phần tử dương của list: {len([i>0 for i in list])}')
print(f'tổng các số hạng dương trong list là: {sum([i>0 for i in list])}')
for i in range(0,len(list)):
    if list[i]<0:
        print(f'phần tử âm đầu tiên của list ở vị trí: {i} ')
        break
for i in range(len(list)-1,0,-1):
    if list[i]>0:
        print(f'phần tử dương cuối cùng của list ở vị trí: {i} ')
        break
a=max(list)
print(f'phần tử lớn nhấn cảu list là: {a}')
print(f'phần tử lớn nhất của list ở vụ trí: {list.index(a)}')