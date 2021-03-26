def trojkat(a,b,c):
    if a*a +b*b==c*c or a*a+c*c==b*b or c*c+b*b==a*a:
        print("Trojkat jest prostokatny")
    else:
        print("Trojkat nie jest prostokatny")
trojkat(4,5,7)
trojkat(1,2,3)
trojkat(3,4,5)