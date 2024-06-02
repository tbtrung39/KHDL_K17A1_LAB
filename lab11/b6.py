bang = [
    [4],
    [211,133,180,5],
    [192,168,1,254],
    [11,1,11,233]
]
with open('bang.txt','w') as file:
    for row in bang:
        file.write(''.join(map(str,row))+'\n')
with open('bang.txt','r') as file:
    dong = file.readlines()
    print("dong dau tien:",dong[0].strip())
    print("dong thu ba:",dong[2].strip())
with open('bang.txt','r') as file:
    toan_bo = file.read()
    print("\n Noi dung toan bo file:",toan_bo)
A =[]
for row in bang:
    row = [str(num) if num % 2 != 0 else '0' for num in row]
    A.append(row)
file_names = 'ODD.txt'
with open(file_names,'w') as file:
    for row in A:
        file.write(''.join(row)+'\n')

with open(file_names,'r') as file:
    file_odd = file.read()
    print("\n Noi dung file odd.txt:",file_odd)