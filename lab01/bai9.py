n = int(input("Nhập vào số lần tung xúc sắc n:"))
def xac_suat_cua_it_nhat_mot_6(n):
    tong_ket_qua=6**3
    ket_qua_khong_co_6=5**3
    xac_suat_khong_co_6= ket_qua_khong_co_6/tong_ket_qua
    xac_suat_cua_it_nhat_mot_6=1-xac_suat_khong_co_6
    xac_suat=1-(1-xac_suat_cua_it_nhat_mot_6)**n
    return round(xac_suat, 2)
ket_qua= xac_suat_cua_it_nhat_mot_6(n)
print("xác suất khi tung n lần 3 xúc sắc là:", ket_qua)
