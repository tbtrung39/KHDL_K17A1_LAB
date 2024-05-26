
def loc(chuoi):
    b=str()
    for i in chuoi:
        if 47 < ord(i) < 58 or 64< ord(i) <71:
            b+=i
    return b    

def test(so):
    try:
        int(so, 2)
        print(f"chuỗi {so} là biểu diễn cơ số 2.")
    except ValueError:
        try:
            int(so, 8)
            print(f"chuỗi {so} là biểu diễn cơ số 8.")
        except ValueError:
            try:
                int(so, 10)
                print(f"chuỗi {so} là biểu diễn cơ số 10.")
            except ValueError:
                try:
                    int(so, 16)
                    print(f"chuỗi {so} là biểu diễn cơ số 16.")
                except ValueError:
                    print(f"chuỗi {so} không phải là biểu diễn của bất kỳ cơ số nào.")

def chuyen_doi_2_sang_10(chuoi):
    return int(chuoi, 2)

def chuyen_doi_8_sang_10(chuoi):
    return int(chuoi, 8)

def chuyen_doi_16_sang_10(chuoi):
    return int(chuoi, 16)