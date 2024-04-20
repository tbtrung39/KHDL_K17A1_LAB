import msvcrt
tap_hop=set()
while True:
  ki_tu=input("nhap vao cac ki tu(ket thuc bang phim ESC):")
  ki_tu=msvcrt.getch().decode("utf-8")
  if ki_tu=="ESC":
    break
  tap_hop.add(ki_tu)
loai_bo={char for char in tap_hop if not ki_tu.issdigit()}
print("tap_hop :",loai_bo)