import random
cn = ["Anh", "Em"]
dt = ["Chơi", "Yêu"]
tn = ["Bóng đá", "Bóng rổ"]
cau = f"{random.choice(cn)} {random.choice(dt)} {random.choice(tn)}"
print(f"Câu hoàn chỉnh là: {cau}")