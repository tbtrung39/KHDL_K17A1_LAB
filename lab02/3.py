day =  int(input('nhập ngày trong tuần ở đây nhé : '))
if 0<day <=7:
    if day ==1:
        print(day,'Sunday')
    elif day  == 2:
        print(day,'Monday')
    elif  day  ==  3:
        print(day,'Tuesday')
    elif day == 4:
        print(day,'Wednesday')
    elif day ==5:
        print(day,'Thursday')
    elif day == 6:
        print(day,'Friday')
    elif  day == 7 :
        print(day,'Saturday')
else:
    print('trong tuần k có thứ đấy ')