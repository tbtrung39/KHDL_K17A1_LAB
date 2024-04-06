import random

A = []
for i in range(1000):
    random_so = random.randint(1,9999)
    A.append(random_so)
#dung sorted    
print(sorted(A))
#khong dung sorted
sap_xep_ko_sorted = A.copy()
for i in range(len(sap_xep_ko_sorted)):
    for j in range(i+1,len(sap_xep_ko_sorted)):
        if sap_xep_ko_sorted[i] > sap_xep_ko_sorted[j]:
            sap_xep_ko_sorted[i],sap_xep_ko_sorted[j] = sap_xep_ko_sorted[j],sap_xep_ko_sorted[i]
print('Danh sách ko sử dụng hàm sorted :', sap_xep_ko_sorted)           
