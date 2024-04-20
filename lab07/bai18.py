tcdt = {}
n = int(input("nhập vào số lượng thí sinh: "))
for i in range(n):
    sbd = int(input(f"nhập vào số báo danh của thí sinh số {i + 1}: "))
    name = str(input(f"nhập vào tên của thí sinh số {i + 1}: "))
    score = float(input(f"nhập vào điểm thi của thí sinh số {i + 1}: "))
    tcdt[sbd] = {"name":name,"score":score}
a = int(input("nhập vào sbd của thí sinh cần kiểm tra: "))
if a in tcdt:
    ts = tcdt[a]
    print(f"số báo danh của thí sinh đó là {a}")
    print(f"họ và tên của thí sinh đó {ts['name']}")
    print(f"điểm của thí sinh đó {ts['score']}")
else:
    new_name = str(input("nhập vào tên của thí sinh mới}: "))
    new_score =  float(input("nhập vào điểm thi của thí sinh mới: "))
    tcdt[a] = {"name":new_name,"score":new_score}
print(tcdt)