import os

def read_passengers(filename):
    if not os.path.isfile(filename):
        print(f"File {filename} not found.")
        return None, None
    with open(filename, 'r') as file:
        lines = file.readlines()
    num_passengers = int(lines[0].strip())
    weights = [list(map(float, line.strip().split())) for line in lines[1:num_passengers + 1]]
    return num_passengers, weights

def write_weight_out(filename, weights):
    with open(filename, 'w') as file:
        for weight in weights:
            file.write(f"{sum(weight):.2f}\n")

def write_canceled_out(filename, weights):
    with open(filename, 'w') as file:
        for i, weight in enumerate(weights):
            if sum(weight) > 23 or len(weight) > 5:
                file.write(f"{i+1}\n")

def main():
    # Đảm bảo đường dẫn tuyệt đối tới tệp
    input_file = os.path.join('C:', 'Users', 'MY PC', 'Desktop', 'NGUYỄN VĂN PHÚC', 'lab11', '9', 'PASSENGERS.IN')
    output_weight_file = os.path.join('C:', 'Users', 'MY PC', 'Desktop', 'NGUYỄN VĂN PHÚC', 'lab11', '9', 'WEIGHT.OUT')
    output_canceled_file = os.path.join('C:', 'Users', 'MY PC', 'Desktop', 'NGUYỄN VĂN PHÚC', 'lab11', '9', 'CANCELED.OUT')

    num_passengers, weights = read_passengers(input_file)
    if num_passengers is not None and weights is not None:
        write_weight_out(output_weight_file, weights)
        write_canceled_out(output_canceled_file, weights)

if __name__ == "__main__":
    main()
