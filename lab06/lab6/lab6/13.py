CN = ["Cô ấy","Anh ấy"]
DT = ["yêu","yêu"]
TN = ["hoa","lá"]

cau = tuple(f"{chu_ngu},{dong_tu},{tan_ngu}" for chu_ngu in CN for dong_tu in DT for tan_ngu in TN)

print("Tất cả các câu có thể tạo là:",cau)