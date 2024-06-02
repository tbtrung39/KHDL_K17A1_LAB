ss=["Anh","Em"]
vs=["Choi","Yêu"]
os=["Bóng đá","Bóng rổ"]
cau=[(s,v,o), for s in ss for v in vs for o in os]
for cau in cau:
    print("".join(cau))