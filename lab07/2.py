numbers=[]
while True:
  num=input("Nhap vao cac so tu nhien:")
  while num.isalpha():
    num=input("day khong phai tu nhien vui long nhap lai:")
  if num==".":
    break
  numbers.append(num)
A=set(numbers)
print("Tap hop a:",A)