import random

numero = print(random.randint(3, 9))
#print(random.choices([2, 4, 7, 9, 0, 3]))
intentos = 0
while True: 
    valor = input("Ingrese su numero")
    if valor == numero:
        print("Felicitaciones Has acertado y ganado el juego")
        break
    else: 
        print("Lo sentimos has fallado")
        intentos += 1
    if intentos > 5:
        print()