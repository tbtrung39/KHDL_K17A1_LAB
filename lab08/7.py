def find_lagest_smallest_number(a,b,c):
    a1 = max(a,b,c)
    a2 = min(a,b,c)
    return a1,a2
s1 = int(input("Enter a:"))
s2 = int(input("Enter b:"))
s3 = int(input("Enter c:"))
a1,a2 = find_lagest_smallest_number(s1,s2,s3)
print(f"max number:{a1}")
print(f"min number:{a2}")