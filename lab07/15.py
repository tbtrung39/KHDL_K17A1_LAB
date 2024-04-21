# Hai danh sách ban đầu
list1 = ['a0', 'a1', 'a2']
list2 = ['ten0', 'ten1', 'ten2']
tu_dien = {}
for i in range(len(list1)):
    tu_dien[list1[i]] = list2[i]

for a , value in tu_dien.items():
    print(f"{a} : {value}")
