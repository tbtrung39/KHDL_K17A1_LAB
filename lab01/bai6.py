diem_A = tuple(map(float, input("Nhập tọa độ của điểm A (x, y): ").split()))
diem_B = tuple(map(float, input("Nhập tọa độ của điểm B (x, y): ").split()))
diem_C = tuple(map(float, input("Nhập tọa độ của điểm C (x, y): ").split()))

trung_diem_AB = ((diem_A[0] + diem_B[0]) / 2, (diem_A[1] + diem_B[1]) / 2)
trung_diem_BC = ((diem_B[0] + diem_C[0]) / 2, (diem_B[1] + diem_C[1]) / 2)
trung_diem_CA = ((diem_C[0] + diem_A[0]) / 2, (diem_C[1] + diem_A[1]) / 2)
trong_tam_x = (trung_diem_AB[0] + trung_diem_BC[0] + trung_diem_CA[0]) / 3
trong_tam_y = (trung_diem_AB[1] + trung_diem_BC[1] + trung_diem_CA[1]) / 3
trong_tam = (round(trong_tam_x, 2), round(trong_tam_y, 2))
print("Tọa độ của trọng tâm là:", trong_tam)