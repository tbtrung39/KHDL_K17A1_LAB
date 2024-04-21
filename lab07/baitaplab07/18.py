students = {
    123: ("Nguyễn Mạnh Cường", 8),
    456: ("Trần Bảo Vy", 7),
    789: ("Trịnh Đức Minh", 9)
}


student_id = int(input("Nhập số báo danh của thí sinh: "))

if student_id in students:
    name, score = students[student_id]
    print(f"Họ và tên: {name}, Điểm thi: {score}")
else:
    name = input("Nhập họ và tên của thí sinh: ")
    score = float(input("Nhập điểm thi của thí sinh: "))
    students[student_id] = (name, score)
    print("Thông tin thí sinh đã được thêm vào từ điển.")
print("Thông tin thí sinh sau khi nhập:")
for student_id, (name, score) in students.items():
    print(f"Số báo danh: {student_id}, Họ và tên: {name}, Điểm thi: {score}")