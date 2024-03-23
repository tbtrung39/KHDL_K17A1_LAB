day = int(input("Enter a day:"))
month = int(input("Enter a month:"))
year = int(input("Enter a year:"))
if month == 1:
    day_fake = 31
elif month == 2:
    day_fake = 28
elif month == 3:
    day_fake = 31
elif month == 4:
    day_fake = 30
elif month == 5:
    day_fake = 31
elif month == 6:
    day_fake = 30
elif month == 7:
    day_fake = 31
elif month == 8:
    day_fake = 31
elif month == 9:
    day_fake = 30
elif month == 10:
    day_fake = 31
elif month == 11:
    day_fake = 30
elif month == 12:
    day_fake = 31
else:
    print("please,Try enter again:")
if day<day_fake:
    day+=1
else:
    day=1
    if month<12:
        month+=1
    else:
        month = 1
        year+=1
print(f"Ngày {day}",end=" ")
print(f"Tháng {month}",end=" ")
print(f"Năm {year}",end=" ")