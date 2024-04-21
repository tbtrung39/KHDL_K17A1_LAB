tcdt = {}
n = int(input("Nhập vào số lượng thí sinh: "))
for i in range(n):
    sbd = int(input(f"Nhập vào số báo danh của thí sinh số {i + 1}: "))
    name = str(input(f"Nhập vào tên của thí sinh số {i + 1}: "))
    score = float(input(f"Nhập vào điểm thi của thí sinh số {i + 1}: "))
    tcdt[sbd] = {"Name": name, "Score": score}
a = int(input("nhập vào sbd của thí sinh cần kiểm tra: "))
if a in tcdt:
    ts = tcdt[a]
    print(f"Số báo danh của thí sinh đó là {a}")
    print(f"Họ và tên của thí sinh đó {ts['Name']}")
    print(f"Điểm của thí sinh đó {ts['Score']}")
else:
    new_name = str(input("Nhập vào tên của thí sinh mới: "))
    new_score =  float(input("Nhập vào điểm thi của thí sinh mới: "))
    tcdt[a] = {"Name": new_name, "Score": new_score}
print(tcdt)