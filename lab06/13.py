#Yeu cau: Tao cac cau tu chu ngu, dong tu, tan ngu
chu_ngu=["Anh","Em"]
dong_tu=["Choi","Yeu"]
tan_ngu=["Bong da","Bong ro"]

cac_cau=[]

for cn in chu_ngu:
    for dt in dong_tu:
        for tn in tan_ngu:
            cau= cn +" "+ dt +" "+ tn +"."
            cac_cau.append(cau)

for cau in cac_cau:
    print(cau)