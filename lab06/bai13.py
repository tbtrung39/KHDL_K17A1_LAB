import random
cn = ["Anh","Em"]
dt = ["Chơi","Yêu"]
tn = ["Bóng đá","Bóng rổ"]
tap_cau = []
for i in cn:
    for j in dt:
        for z in tn:
            cau = f"{i} {j} {z}"
            print(f"câu hoàn chỉnh là: {cau}")