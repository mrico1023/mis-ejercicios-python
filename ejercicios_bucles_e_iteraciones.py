numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print("Numero",number)

palabra = "python"
for pal in palabra:
    print(pal)

for i in range(10):
    print("Valor de i",i)

for i in range(2,6):
    print("Valor de i:", i)

for i in range(0,21,2):
    print("El valor de i es:",i)

persona = {"Nombre": "David", "Edad": 36, "Ciudad": "Bogotá"}
for datos, valor in persona.items():
    print(datos, ":", valor)

#Ejercicio 1: Imprimir una lista de números
numeros = [1, 2, 3, 4, 5]
for i in numeros:
    print(i)

#Ejercicio 2: Imprimir cada letra de una palabra
palabra = "Python"
for pal in palabra:
    print(pal)

#Ejercicio 3: Sumas números en una lista
numeros = [10, 20, 30, 40]
suma = 0
for numero in numeros:
    suma = suma + numero
print("La suma total es de: ",suma)

#Ejercicio 4: Multiplicar cada elemento por 2
numeros = [2, 4, 6, 8, 10]
multiplicación = []
for numero in numeros:
    multiplicación.append(numero*2)
print("El resultado de la multiplicación es: ",multiplicación)

#Ejercicio 5: Contar letras en una palabra
palabra = "banano"
contador = 0
for letra in palabra:
    contador +=1
print("La palabra contiene",contador,"letras")

#Ejercicio 6: Filtrar números pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero )
print(pares)

#Ejercicio 7: Contar vocales en una frase
frase = "Hola, ¿Como estas?"
vocales = "aeiou"
contador = 0
for letra in frase:
    if letra in vocales:
        contador +=1
print("La frase tiene",contador,"vocales")




