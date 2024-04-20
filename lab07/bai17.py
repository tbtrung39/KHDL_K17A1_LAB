ttsv = {}
n = int(input("nhập vào số lượng sinh viên: "))
for i in range(n):
    msv = int(input(f"nhập vào mã sinh viên gồm 6 ký tự của sinh viên số {i + 1}: "))
    msv = str(msv)
    while len(msv) != 6:
        print("mã sinh viên phải gồm 6 ký tự")
        msv = int(input(f"nhập lại mã sinh viên gồm 6 ký tự của sinh viên số {i + 1}: "))
        msv = str(msv)
    name = str(input(f"nhập vào tên của sinh viên số {i + 1}: "))
    score = float(input(f"nhập vào điểm thi của sinh viên số {i + 1}: "))
    ttsv[msv] = {"name":name,"score":score}