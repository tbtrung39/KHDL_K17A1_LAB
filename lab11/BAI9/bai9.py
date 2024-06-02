def read_passengers(filename):
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
    num_passengers, weights = read_passengers('D:/LAB11/BAI9/PASSENGERS.IN')
    write_weight_out('D:/LAB11/BAI9/WEIGHT.OUT', weights)
    write_canceled_out('D:/LAB11/BAI9/CANCELED.OUT', weights)

if __name__ == "__main__":
    main()
