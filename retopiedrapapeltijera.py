print("Bienvenido al clásico juego de piedra papel o tijera")
jugador1 = input("Escoge entre piedra, papel o tijera: ")
jugador2 = input("Escoge entre piedra, papel o tijera: ")
#seleccion_usuario = ["piedra", "papel", "tijera"]

if jugador1 == jugador2:
    print("Es un empate")
elif jugador1 == "piedra" and jugador2 == "tijera":
    print("Jugador 1 gana")
elif jugador1 == "papel" and jugador2 == "piedra":
    print("Jugador 1 gana")
elif jugador1 == "tijera" and jugador2 == "papel":
    print("Jugador 1 gana")
else:
    print("Jugador 2 gana")


