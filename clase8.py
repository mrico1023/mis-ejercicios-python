to_do = ["Dirigirnos al hotel", 
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]
print(to_do)
numbers = [1,2,3,4, "cinco"]
print(numbers)
print(type(numbers))
mix = ["uno", 2, 3.14, True, [1,2,3]]
print(mix)
print(len(mix))
print("Primer elemento: ", mix[0])
string = "Hola Mundo"
print("Primer elemento:", string[0])
print(mix)
mix.append(False)
print(mix)
print(mix.index(2))
numbers = [1,2,90.5,4,5,100]
print(numbers)
print("Mayor", max(numbers))
print("Menor", min(numbers))
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)
del numbers
print(numbers)