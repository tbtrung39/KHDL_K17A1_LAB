import os
print("\n     VUI LONG CHON MENU")
while True:
    print("________________________________________________")
    print("|[1] Cafe                                       |")
    print("|[2] Cam Vat                                    |")
    print("|[3] Nuoc ep ca rot                             |")
    print("|[4] Nuoc loc                                   |")
    print("|[5] Nuoc Dua                                   |")
    print("|[0] Bam so 0 de thoat                          |")
    print("________________________________________________")
    chon = int(input("goi do trong MENU: "))
    if chon ==1:
        print("ban da chon Cafe")
    elif chon ==2:
        print("Ban da chon Cam Vat")
    elif chon ==3:
        print("Ban do chon Nuoc ep ca rot")
    elif chon ==4:
        print("Ban da chon Nuoc loc")
    elif chon ==0:
        break
    else:
        print("Vui long chon tu 1-5")
    tt= input("nhap so bat ky de tiep tuc, nhap 0 de thoat: ")
    if tt == "0":
        break
    else:
        os.system('cls')