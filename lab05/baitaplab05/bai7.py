van_ban = input("enter in document:")
tu_can_tim = input("enter the word you want the search:")
a = van_ban.lower()
tach_text = a.split()
count=0
for i in tach_text:
    if i == tu_can_tim.lower():
        count+=1
print("Number of occurrences of the word to search:",count)
