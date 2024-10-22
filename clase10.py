numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])
information = {"Nombre": "Marlon",
               "Apellido": "Rico",
               "Altura:" : 1.69,
               "Edad": 36}
print(information)
del information["Edad"]
print(information)
claves = information.keys()
print(claves)
print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = {"Marlon":{"Apellido": "Rico",
               "Altura:" : 1.69,
               "Edad": 36},
               "Luz":{"Apellido": "Gomez",
               "Altura:" : 1.65,
               "Edad": 46}}
print(contacts["Marlon"])