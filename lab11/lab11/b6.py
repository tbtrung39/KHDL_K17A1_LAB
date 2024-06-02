bang = [
    [4],
    [211, 133, 180, 5],
    [192, 168, 1, 254],
    [11, 1, 11, 233]
]

# Write the content of 'bang' to 'bang.txt'
with open('bang.txt', 'w') as file:
    for row in bang:
        file.write(' '.join(map(str, row)) + '\n')

# Read and print the first and third lines of 'bang.txt'
with open('bang.txt', 'r') as file:
    lines = file.readlines()
    print("dong dau tien:", lines[0].strip())
    print("dong thu ba:", lines[2].strip())

# Read and print the entire content of 'bang.txt'
with open('bang.txt', 'r') as file:
    toan_bo = file.read()
    print("\nNội dung toàn bộ file:", toan_bo)

# Create a new list A with odd numbers replaced by '0'
A = []
for row in bang:
    row = [str(num) if num % 2 != 0 else '0' for num in row]
    A.append(row)

file_names = 'ODD.txt'
# Write the content of A to 'ODD.txt'
with open(file_names, 'w') as file:
    for row in A:
        file.write(' '.join(row) + '\n')

# Read and print the content of 'ODD.txt'
with open(file_names, 'r') as file:
    file_odd = file.read()
    print("\nNoi dung file ODD.txt:", file_odd)
