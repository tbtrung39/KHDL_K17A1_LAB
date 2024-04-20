sv_dict = {}
while True:
    msv = input("Nhập mã sinh viên (6 ký tự số): ")
    if len(msv) != 6 or not msv.isdigit():
        print("Mã sinh viên phải là một chuỗi 6 ký tự số. Vui lòng nhập lại.")
        continue
    ten = input("Nhập tên sinh viên: ")
    valid_score = False
    while not valid_score:
        diem_so = input("Nhập điểm số (0-10): ")
        if student_score.isdigit():
            student_score = int(student_score)
            if 0 <= student_score <= 10:
                valid_score = True
            else:
                print("Điểm số phải là một số nguyên trong khoảng từ 0 đến 10. Vui lòng nhập lại.")
        else:
            print("Điểm số phải là một số nguyên trong khoảng từ 0 đến 10. Vui lòng nhập lại.")
    sv_dict[msv] = (ten, student_score)
    cont = input("Bạn có muốn nhập thông tin sinh viên khác không? (y/n): ")
    if cont.lower() != 'y':
        break
sorted_students = sorted(sv_dict.items(), key=lambda x: x[1][1], reverse=True)
# In ra thông tin sinh viên đã sắp xếp
print("\nDanh sách sinh viên đã sắp xếp theo điểm số giảm dần:")
for student_id, (student_name, student_score) in sorted_students:
    print(f"Mã sinh viên: {student_id}, Tên sinh viên: {student_name}, Điểm số: {student_score}")