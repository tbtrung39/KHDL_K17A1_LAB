CN=['Anh', 'Em']
DT=['Choi', 'Yeu']
TN=['Bong da', 'Bong ro']
cau=[(s,v,o) for s in CN for v in DT for o in TN]
for s,v,o in cau:
    print(f'{s} {v} {o} ')