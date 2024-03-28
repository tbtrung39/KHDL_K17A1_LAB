while True:
    print("-------------Menu---------------")
    print("  1. Cafe")
    print("  2. Cam vat")
    print("  3. Nuoc ep ca rot")
    print("  4. Nuoc ep ca chua")
    print("  5. Nuoc loc")
    print("  6. Nuoc dua")
    print("--------------------------------")

    so = int(input("Moi ban chon thuc uong: "))
    if so == 1:
        print("   Ban da chon cafe")
    elif so == 2:
        print("   Ban da chon cam vat")
    elif so == 3:
        print("   Ban da chon nuoc ep ca rot")
    elif so == 4:
        print("   Ban da chon nuoc ep ca chua")
    elif so == 5:
        print("   Ban da chon nuoc loc")
    elif so == 6:
        print("   Ban da chon nuoc dua")
    elif so == 7:
        print("Cam on ban da dat mon. Xin chao va hen gap lai")
        break
    else:
        print("Vui long nhan so tu 1 den 7")