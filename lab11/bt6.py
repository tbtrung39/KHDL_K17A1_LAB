bang = [[4],
        [211, 133, 180, 5],
        [192, 168, 1, 254],
        [11, 1, 11, 233]]
with open('lab11/bang.txt','w') as file:
    for row in bang:
        file.write(','.join(map(str, row)) + '\n')

with open('lab11/bang.txt','r') as file:
    dong = file.readlines()
    print("Dòng đầu tiên:", dong[0].strip())
    print("Dòng thứ 3:", dong[2].strip())

with open('lab11/bang.txt', 'r') as file:
    toan_bo = file.read()
    print("\n Bảng:")
    print(toan_bo)

A = []
for row in bang:
    row = [str(num) if num % 2 != 0 else '0' for num in row]
    A.append(row)

file_name = "lab11/ODD.txt"
with open(file_name,'w') as file_:
    for row in A:
        file_.write(','.join(row) + '\n')

with open(file_name,'r') as file:
    file_odd = file.read()
    print("\n Bảng mới:")
    print(file_odd)
    print("Dòng cuối cùng:", dong[-1].strip())