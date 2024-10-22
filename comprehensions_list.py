squares = [x**2 for x in range(1,11)]
#print("Cuadrados:", squares)

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5)+32 for temp in celsius]
#print("Temperatura en F:", fahrenheit)

#Numeros pares
evens = [x for x in range(1,21) if x%2 ==0]
#print(evens)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
#print(matrix)
#print(transposed)

doubles = [x*2 for x in range(1,11)]
#print(doubles)

palabras = ["sol", "mar", "montaña", "rio", "estrella"]
palabras_filtradas = [palabra.upper() for palabra in palabras if len(palabra)>3]
#print("Palabras filtradas y en mayúsculas:", palabras_filtradas)

claves = ["nombre", "edad", "ocupación"]
valores = ["Juan", 30, "Ingeniero"]
diccionario = {claves[i]: valores[i] for i in range(len(claves))}
#print("Diccionario creado:", diccionario)

juguetes = ["muñeca", "auto", "robot", "tren", "yo-yo"]
juguetes_grandes = [juguete for juguete in juguetes if len(juguete)>4]
#print(juguetes_grandes)

numeros = [x**2 for x in range(1,6)]
#print(numeros)

numeros = [1, 2, 3, 4, 5]
numeros_al_cuadrado = [num**2 for num in(numeros)]
#print(numeros_al_cuadrado)

animales = ["gato", "elefante", "pez", "tigre", "ratón", "lobo"]
animales_cortos = [anim for anim in animales if len(anim)<=4]
#print(animales_cortos)

nombres = ["Ana", "Santiago", "Luis", "Carlos", "Beatriz"]
nombres_largos = [nom.upper() for nom in nombres if len(nom) >5]
#print(nombres_largos)

personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]
filtro_personas = [filtro["nombre"] for filtro in personas if filtro["ciudad"] == "Madrid" and filtro["edad"] > 30]
print(filtro_personas)
