str = "Do Thi Nguyen 4105"
so = ""
for i in str:
    if i.isdigit():
        so += i
print("Chuoi sau khi loai cac chu la: ", so)
if len(str) == len(so):
    print("Chuoi nay la chuoi hoan hao.")
else:
    print("Chuoi nay khong la chuoi hoan hao.")
    
