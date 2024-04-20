# tao set
tap_hop=set()
# nhap and kiem tra
while True:
    ky_tu=input("nhap ky tu")
    if ky_tu.lower()=="esc":
        break
    tap_hop.add(ky_tu)
tap_hop={ky_tu for ky_tu in tap_hop if not ky_tu.isdigit()}
print("phan tu so duoc xoa ra khoi tap hop",tap_hop)