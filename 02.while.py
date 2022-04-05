#La estructura de control while ejecuta un conjunto de sentencias mientras la condición sea verdadera
iterator = 0
while iterator < 10:
    print(iterator)
    iterator += 1

print("#####")

iterator = 10
while iterator > 0:
    print(iterator)
    iterator -= 1

print("#####")

#romper el while con un break
iterator = 0
while iterator < 100:
    print(iterator)
    if iterator == 42:
        break
    iterator += 2

print("####")

#saltarnos un paso con continue
iterator = 0
while iterator < 100:
    iterator += 1
    if iterator % 3 == 0:
        continue     
    print(iterator)
else:
    print("el iterador ya no es menor que 100")
    