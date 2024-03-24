#Số hoàn hảo
n=int(input("Các số hoàn hảo bé hơn hoặc bằng: "))

print(f"Các số hoàn hảo bé hơn hoặc bằng {n} la ")

for nghiem in range(1,n+1) :
    sum=0
    for i in range(1,n):
        if nghiem %i==0:
            sum += i
            if sum>nghiem:
                break
    if sum==nghiem:
        print(nghiem)
        continue
