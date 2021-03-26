#zadanie 3
slownik = {"sok":"litr","ziemniaki":"kg","cukierki":"deko","bułka":"sztuka"}
odwrocone = {value: "sztuka" for value, value in slownik.items()}
szt = slownik.fromkeys(["sztuka"])
print(odwrocone)
print(slownik)
print(szt)
