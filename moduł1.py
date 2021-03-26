def ciag(a=1,b=2,ile=5):
    iloczyn = 1
    for x in range(ile):
        iloczyn *=a*b
        return iloczyn
print(ciag())
print(ciag(ile=3))
print((ciag(2,4,6)))
print("Wzor 1: an=a1+(n−1)⋅r")
print("Wzór 2: Sn=(a1+an2/2)⋅n")
print(ciag())

