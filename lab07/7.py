import random
import string
A = input("nhap tap hop A(cac ky tu chu va so):")
B = input("nhap tap hop B(cac ky tu chu va so):")
set_A = set(A)
set_B = set(B)
phan_tu_chung = set_A.intersection(set_B)
print("cac phan tu chung cua A va B la:",",".join(phan_tu_chung))