#nombre = "johana"
#def saludar():
#    print( f"¡Hola mundo! {nombre}")

#llamar funcion 
#saludar() #imprime ¡Hola, mundo!

#def sumar (a, b):
#    return a + b

#resultado = sumar (5 + 3)
#print(resultado)

def multiplicacion(x,y):
    return x*y
cantidad = 1
subtotal = 0
while cantidad != 0:
    cantidad = int(input("ingrese la cantidad del producto"))
    if cantidad == 0:
        break
    valor = int(input("ingrese el valor del producto"))
    calculo = multiplicacion(valor, cantidad)
    subtotal = subtotal + calculo


print(f"el total a pagar es {subtotal}")
