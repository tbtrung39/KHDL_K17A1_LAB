thi_sinh={
    100: ["Phan Van A",10],
    101: ["Nguyen Thi B",9],
    102: ["Phung Van C",8],
    103: ["Do Thi D",7]
}

so_bao_danh=int(input("Nhap so bao danh:"))
if so_bao_danh in thi_sinh:
    ho_ten, diem =thi_sinh[so_bao_danh]
    print("Ho va ten:",ho_ten)
    print("Diem thi:",diem)
else:
    ho_ten=input("Nhap ho va ten:")
    diem=float(input("Nhap diem thi:"))
    thi_sinh[so_bao_danh] =[ho_ten,diem]
    print("Thong tin thi sinh da duoc bo sung vao tu dien")