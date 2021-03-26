def ciag(a=1,b=2,ile=5):
    iloczyn = 1
    for x in range(ile):
        iloczyn *=a**b
        return iloczyn
print(ciag())
print(ciag(ile=3))
print((ciag(3,6,9)))
print("Wzor na ciag geometryczny to: an=a1⋅qn−1")