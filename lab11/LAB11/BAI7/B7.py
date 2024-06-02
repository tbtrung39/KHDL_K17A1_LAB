def read_integers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

def write_integers_to_file(filename, numbers):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")

def main():
    nums = read_integers_from_file('D:/LAB11/BAI7/n_nums.txt')
    num = read_integers_from_file('D:/LAB11/BAI7/n_num.txt')
    combined_numbers = nums + num
    write_integers_to_file('D:/LAB11/BAI7/so_chung.txt', combined_numbers)

if __name__ == "__main__":
    main()
