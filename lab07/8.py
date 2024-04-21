tap_hop_A={1,2,5,"Hello",3,4,6,"World",5,"Python",6.2}

so_nguyen=sum(isinstance(x,int) for x in tap_hop_A)
so_thuc=sum(isinstance(x,str) for x in tap_hop_A)
so_chuoi=sum(isinstance(x,str) for x in tap_hop_A)

print("So nguyen:",so_nguyen)
print("So thuc:",so_thuc)
print("So chuoi:",so_chuoi)