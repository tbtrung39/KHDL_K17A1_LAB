def main():
    with open("lab11/bai3f_in.dat", mode="r", encoding="utf-8") as file_in:
        dayso=[]
        for line in file_in:
            dayso.append(line.strip().split())
            return dayso

    so_cuc_tri = []
    dem = 0
    for i in range(1, len(dayso) - 1):
        if dayso[i - 1] < dayso[i] > dayso[i + 1]:
            so_cuc_tri.append(dayso[i])
            dem += 1

    try:
        with open("lab11/bai3f_out.dat", mode="w") as file_out:
            chain_cuc_tri = " ".join(map(str, so_cuc_tri))
            file_out.write(str(dem) + "\n")
            file_out.write(chain_cuc_tri)
    except IOError:
        print("Lỗi: Không thể ghi vào tệp đầu ra.")

if __name__ == "__main__":
    main()
