ki_tu_1 = input("nhap ki tu 1: ")
ki_tu_2 = input("nhap ki tu 2: ")
s=""
for j in range(len(ki_tu_1)):
    for i in ki_tu_2:
        if ki_tu_1[j]== i:
            s+= i
print(s)
