#Ejemplo de una función sin valor de retorno
from re import A


def volume(radius):
    v = 4/3 * 3.14 * radius ** 3
    print(v)

enigma = volume(7)
print(enigma)

#Ejemplo de una función con valor de retorno
def area(radius):
    a = 3.14 * radius ** 2
    return a

resultado = area(7)
area(7) #este computo se perdió para siempre ya que no se asignó a ninguna variable
print(resultado)

#Podemos tener más de un retorno por función
def isAdult(age):
    if age < 18:
        return False
    if age >= 18:
        return True

hasBeer = isAdult(18)
print(hasBeer)