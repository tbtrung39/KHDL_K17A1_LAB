print("     CHUONG TRINH GOI DO UONG     ")
while True: 
    print("----------------------------------")
    print("|               MENU             |")
    print("|[1] - Cafe                      |")
    print("|[2] - Cam vat                   |")
    print("|[3] - Nuoc ep ca rot            |")
    print("|[4] - Nuoc loc                  |")
    print("|[5] - Nuoc dua                  |")
    print("----------------------------------")
 
    n = int(input("MOi ban chon do uong "))

    if n == 1 : 
       print("Ban da chon cafee! Xin vui long doi ")
    elif n == 2: 
       print("Ban da chon cam vat! Xin vui long doi ")
    elif n == 3 : 
       print("Ban da chon nuoc ep ca rot! Xin vui long doi ")
    elif n == 4 : 
       print("Ban da chon nuoc loc! Xin vui long doi ")
    elif n == 5 : 
       print("Ban da chon nuoc dua! Xin vui long doi ")
    else: 
       print("Xin moi chon lai ")
       n = int(input("MOi ban chon do uong "))

    print("Quy khach dung ngon mieng ")  