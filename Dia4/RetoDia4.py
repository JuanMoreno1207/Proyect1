from random import *
nombre = input("Ingresa tu nombre, por favor : ")
numeroCal = randint(1,100)
vidas = 8
print(f"Bienvenido {nombre}, Diviertete!")
while vidas > 0:
    numeroU = int(input("Adivina un número del 1 a 100 :  "))
    vidas -= 1
    if numeroU not in range(1,101):
        print("¡Te equivocaste! número no permitido")
    elif numeroU < numeroCal:
        print("¡Te equivocaste! número menor al numero correcto")
    elif numeroU > numeroCal:
        print("¡Te equivocaste! número mayor al numero correcto")
    else:
        print(f"¡Ganaste! El numero correcto es {numeroCal}, lo lograste adivinar en el intento {8-vidas}")
        break
    print(f"Tienes {vidas} vidas")
else:
    print(f"Se acabaron las vidas, ¡GAME OVER! el numero correcto era {numeroCal}")


