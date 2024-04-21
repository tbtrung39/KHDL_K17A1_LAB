'''
Cho hai danh sách listi gồm n số khác nhau [ao, ,.., ân-I] và danh sách list2 gồm n tên (teno, ten ,.., ten). 
Viết chương trình tạo ta một từ điển với các phần tử có dạng10:20/-strong/-heart:>:o:-((:-hĐã gửi
Xem trước khi gửiThả Files vào đây để xem lại trước khi gửi
'''
list1 = ['a0', 'a1', 'a2']
list2 = ['ten0', 'ten1', 'ten2']
tu_dien = {}
for i in range(len(list1)):
    tu_dien[list1[i]] = list2[i]

for a , value in tu_dien.items():
    print(f"{a} : {value}")
