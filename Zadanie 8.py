def zakupy(**produkt):
    suma = 0
    for x in produkt:
        suma +=1
        print(produkt)
        print("Suma produktow",suma)
        return suma(produkt.values())