def giai_phuong_trinh_bac1(a, b):
    if a == 0:
        if b == 0:
            return "Phuong trinh vo so nghiem"
        else:
            return "Phuong trinh vo nghiem"
    else:
        x = -b / a
        return x
