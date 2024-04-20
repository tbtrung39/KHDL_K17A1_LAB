n=int(input("Nhap so N"))
while n<=0:
  n=int(input("Nhap lai n:"))
nguyento=[]
num=2
while len(nguyento)<n:
  isnguyento=True
  for i in range(2,int(num**0.5)+1):
    if num%i==0:
      isnguyento=False
      break
  if isnguyento:
    nguyento.append(num)
  num+=1
print("day",n,"so nguyen to dau tien:",nguyento)