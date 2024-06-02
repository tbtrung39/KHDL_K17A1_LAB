def chinh():
    try:
        with open("lab11/bai3f_in.dat", mode="r", encoding="utf-8") as file_in:
            day_so = []
            for dong in file_in:
                day_so.extend(map(int, dong.strip().split()))
        
        so_cuc_tri = []
        dem = 0
        for i in range(1, len(day_so) - 1):
            if day_so[i - 1] < day_so[i] > day_so[i + 1]:
                so_cuc_tri.append(day_so[i])
                dem += 1

        try:
            with open("lab11/bai3f_out.dat", mode="w", encoding="utf-8") as file_out:
                chuoi_cuc_tri = " ".join(map(str, so_cuc_tri))
                file_out.write(str(dem) + "\n")
                file_out.write(chuoi_cuc_tri)
        except IOError:
            print("Lỗi: Không thể ghi vào tệp đầu ra.")
    except IOError:
        print("Lỗi: Không thể đọc tệp đầu vào.")

if __name__ == "__main__":
    chinh()
