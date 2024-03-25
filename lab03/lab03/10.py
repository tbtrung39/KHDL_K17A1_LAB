n=int(input("Nhập số nguyên dương:"))
print("Dạng phân tích của",n,"là:",end=" ")
for i in range(2,n+1):
    for j in range(2,i+1):
        if i%j==0 and i==j:
           if n%i==0:
             print(i,end="")
             n//=i
        elif i%j==0:
           break   
    if n==1:    
       break