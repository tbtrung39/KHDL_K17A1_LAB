import random
A = set(input("Nhap cac phan tu cua tap hop A,cach nhau bang dau phay:").split())
B = set(input("Nhap cac phan tu cua tap hop B,cach nhau bang dau cach:").split())
phan_tu_chung = A.intersection(B)
print("cac phan tu chung cua tap hop A va B la:",phan_tu_chung)