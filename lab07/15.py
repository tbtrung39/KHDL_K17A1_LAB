# cho 2 danh sách list 1 gồm n số khác nhau [a0,a1,...,an-1] và danh sách list 2 gồm n tên [ten0,ten1,...,tenn] viết chương trình tạo ra 1 từ điển với các phần tử có dạng <ai>:<teni> in ra nội dung của từ điển # Danh sách số
# Danh sách số
numbers = [1, 2, 3, 4] 
names = ['a', 'b', 'c', 'd'] 
result_dict = {}
for i in range(len(numbers)):
    result_dict[numbers[i]] = names[i]
print(result_dict)