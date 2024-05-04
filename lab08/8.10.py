def  uoc_so ( n ):
    print ( " Các ước tính của số nguyên dương" , n , "là:" )
    for i in range( 1 , n + 1 ):
        if  n  %  i  ==  0 :
            print(i)
n = int(input("Nhap so nguyen duong: "))
uoc_so(n)