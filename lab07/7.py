import random

a = set(str(input("Nhap ki tu chu va so cho tap hop A:")))
b = set(str(input("Nhap ki tu chu va so cho tap hop B:")))

tap_hop_chung = a.intersection(b)
print("Tap hop chung cua 2 tap hop la:",tap_hop_chung)