so_gio = int(input("nhap so gio:"))
if so_gio <= 3:
    tien = 100000
    tien = tien *so_gio
    print("so tien phai tra la:",tien)
elif so_gio > 3:
    tien = 100000
    so_tien_khuyen_mai = (tien* so_gio)*0.25
    print("so tien khuyen mai va phai tra la ", so_tien_khuyen_mai)
elif 11< so_gio and so_gio <15:
    tien = 100000
    so_tien_khuyen_mai_moi = (so_gio* 0.35)
    print("so tien khuyen mai phai tra la",so_tien_khuyen_mai_moi)