bang = [
    [4],
    [211, 133, 180, 5],
    [192, 168, 1, 254],
    [11, 1, 11, 233]
]

with open('lab11/bang.txt', 'w') as f:
    for row in bang:
        f.write(','.join(map(str, row)) + '\n')

with open('lab11/bang.txt', 'r') as f:
    dong = f.readlines()
    print("dong dau: ", dong[0].strip())
    print("dong ba: ", dong[2].strip())

with open('lab11/bang.txt', 'r') as f:
    toan_bo = f.read()
    print("\n noi dung: ")
    print(toan_bo)

A = []
for row in bang:
    row = [str(num) if num % 2 != 0 else '0' for num in row]
    A.append(row)

file_name = "lab11/ODD.txt"
with open(file_name , 'w') as file_:
    for row in A:
        file_.write(','.join( row) + '\n')

with open (file_name, 'r') as file:
    file_odd = file.read()
    print("\n noi dung")
    print(file_odd)