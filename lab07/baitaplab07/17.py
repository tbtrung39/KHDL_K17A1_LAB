students = {}
while True:
    student_id = input("Nhập mã sinh viên (6 kí tự số): ")
    if not student_id.isdigit() or len(student_id) != 6:
        print("Mã sinh viên phải là một chuỗi gồm 6 kí tự số. Vui lòng nhập lại.")
        continue
    student_name = input("Nhập tên sinh viên: ")
    while True:
        try:
            score = float(input("Nhập điểm số (từ 0 đến 10): "))
            if 0 <= score <= 10:
                break
            else:
                print("Điểm số phải thuộc khoảng từ 0 đến 10. Vui lòng nhập lại.")
        except ValueError:
            print("Điểm số phải là một số. Vui lòng nhập lại.")
 #   rounded_score = round(score)
 #   if rounded_score not in students:
  #      students[rounded_score] = []
   # students[rounded_score].append((student_id, student_name, score))

    cont = input("Bạn có muốn nhập thêm thông tin sinh viên không? (yes/no): ")
    if cont.lower() != 'yes':
        break
print("\nThống kê và sắp xếp sinh viên theo điểm giảm dần:")
sorted_scores = sorted(students.keys(), reverse=True)
for score in sorted_scores:
    print(f"Điểm {score}:")
    for student in students[score]:
        print(f"Mã sinh viên: {student[0]}, Tên sinh viên: {student[1]}, Điểm số: {student[2]}")