def find_prime_number(n):
    if n<=1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
def less_than_n(n1):
    for i in range(2,n1):
        if find_prime_number(i):
            print(i,end=" ")
n2 = int(input("Enter prime number:"))
print(less_than_n(n2))
    