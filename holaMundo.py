print ("hola mundo")

def calcular(cantidad, valor):
    return cantidad * valor
total = calcular
print(f"El total de los productos es {total}")
subtotal = 0
cantidad = 1

while cantidad != 0:
    print("Ingrese la cantidad del producto")
    cantidad = float(input())
    if cantidad == 0:
        break
    print("Ingrese el valor del producto")
    valor = float(input())
    total = calcular(cantidad, valor)
    subtotal += total
    #realizar para solicitar el iva
    
print(f"El total de productos es {subtotal}")
