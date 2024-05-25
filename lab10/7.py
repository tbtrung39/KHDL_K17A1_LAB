import sys
sys.path.append("lab10\packages")
import packages
n = int(input("n: "))
day_so = packages.day_so(n)
print(day_so)
print("chia hết cho 7; ", packages.so_nguyen_to_chia_het_7(day_so))
print("tổng số lẻ: ", packages.tong_so_le(day_so))
print("kiểm tra số chính phương: ", packages.so_chinh_phuong_trong_day(day_so))