#Ejemplo de estructura para iterar secuencias de cosas
#Listas

from numpy import size


drinks = ["mojito","margarita","piña colada"]
for drink in drinks:
    print(drink)

print("####")

#El for tambien funciona con letter
for letter in "tio Charlie":
    print(letter) 

print("####")

#El for tambien puede ser utilizado con el break
for drink in drinks:    
    if drink == "margarita":
        continue
    print(drink)
else:
    print("Berta se terminó los tragos")

print("####")

#for anidados
sizes = ["normal","large","tio Charlie xl"]
for size in sizes:
    for drink in drinks:
        print(drink,size)