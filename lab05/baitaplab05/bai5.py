str = input("Enter a string:")
s1 = " "
for i in str:
    if i.isnumeric():
        s1+=i
s1 = int(s1)
tong = 0
for i in range(1,s1):
    if s1%i==0:
        tong+=i
if tong == s1:
    print(s1,"Là số hoàn hảo")
else:
    print(s1,"không phải là số hoàn hảo")