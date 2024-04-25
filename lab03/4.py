n = int(input("Nhập n là:"))
if n < 2:
    print(n,"không phải là số nguyên tố")
else:
    print("các số nguyên tố bé hơn hoặc bằng",n)
    for i in range (2,n+1):
            j = True
            for k in range (2,int(i**0.5)+1):
                if i % k == 0:
                    j = False
                    break
            if j:
                print(i,end =' ')
                print("\r")