n = input("Nhập chuỗi ký tự: ")
max = 0
maxb = ""
do_dai = 1
do_dai_kt = n[0]
for i in range(1, len(n)):
    if n[i] == do_dai_kt:
        do_dai += 1
    else:
        if do_dai > max:
            max = do_dai
            maxb = do_dai_kt * max
        do_dai_kt = n[i]
        do_dai = 1
if do_dai > max:
    max = do_dai
    maxb = do_dai_kt * max
print("Chuỗi con có độ dài cực đại và bao gồm các phần tử giống nhau:", maxb)