print("\n CHUONG TRINH GOI DO UONG.")
while True:
    print('          Menu chon do uong         ')
    print('1.Cafe                              ')
    print('2.Cam vat                           ')
    print('3.Nuoc ep ca rot                    ')
    print('4.Nuoc loc                          ')
    print('5.Nuoc dua                          ')
    chon=int(input("Chon do uong ma ban muon: "))
    if chon ==1:
        print("Ban da chon cafe")
    if chon ==2:
        print("Ban da chon cam vat")
    if chon ==3:
        print("Ban da chon nuoc ep ca rot")
    if chon ==4:
        print("Ban da chon nuoc loc")
    if chon ==5:
        print("Ban da chon nuoc dua")
    else:
        print("Chi chon do uong tu 1 den 5")
    tt=input("nhap phim bat ky de tiep tuc, bam so 0 de thoat.")
    if tt=="0":
        break