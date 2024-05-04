def nam_nhuan(n):
    return (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0)
def max_day(m,n):
    if m in [1,3,5,7,8,10,12]:
        return 31
    elif m in [4,6,9,11]:
        return 30
    elif m == 2:
        return 29 if nam_nhuan(n) else 28
    else:
        return "Invalid month"
n = int(input("Enter a year:"))
m = int(input("Enter a month:"))
print(f"Year {n} {'là' if nam_nhuan(n) else 'not'} năm nhuận")
print(f"number the most in year {max_day(m,n)}")

