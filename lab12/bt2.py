def docvaghitaptin():
    try:
        tentaptindoc = input("nhap ten tap tin can doc: ")
        tentaptinghi = input("nhap ten tap tin de ghi: ")
        try:
            taptindoc = open(tentaptindoc, mode='r')
        except FileNotFoundError:
            print("khong tim thay tap tin can doc")
            return
        except IOError:
            print("loi khi mo tap tin can doc")
            return
        
        try:
            taptinghi = open(tentaptinghi, mode='w')
        except IOError:
            print("loi khi mo tap tin de ghi")
            taptindoc.close()
            return
        
        try:
            noidung = taptindoc.read()
            taptinghi.write(noidung)
        except Exception as e:
            print(f"loi trong qua trinh doc/ghi: {e}")
        finally:
            taptindoc.close()
            taptinghi.close()
            print("dong cac tap tin truoc khi ket thuc chuong trinh")
    except Exception as e:
        print(f"loi khong xac dinh: {e}")

docvaghitaptin()
