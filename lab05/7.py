Str1="Mùa xuân nho nhỏ"
n=input("Nhap 1 tu don:")
if n.isalpha() and n==n.replace("",""):
  print("co",Str1.count(n),"tu",n)
else:
  print("Khong phải là từ đơn",n)

