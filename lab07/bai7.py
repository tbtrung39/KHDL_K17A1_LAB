import random
import string
A=input("nhap mot chuoi ky tu bat ky: ")
B=input("nhap mot chuoi ky tu bat ky: ")
set_A=set(A)
set_B=set(B)
phan_tu_chung=set_A.intersection(set_B)
print(phan_tu_chung)