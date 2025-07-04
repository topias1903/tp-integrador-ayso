#definicion de la funcion para sumar
def suma(a, b):
    return a + b

#definicion de la funcion para restar
def resta(a, b):
    return a - b

#definición de la funcion para multiplicar
def multiplicacion(a, b):
    return a * b

#definicion de la funcion para dividir
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"


print("Calculadora")
a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))


operacion = input("Ingrese la operación que desea realizar (suma, resta, multiplicacion, division): ").lower()

#condicion que ejecuta la operacion ingresada
if operacion == "suma":
    print(f"{a} + {b} = {suma(a,b)}")
elif operacion == "resta":
    print(f"{a} - {b} = {resta(a,b)}")
elif operacion == "multiplicacion":
    print(f"{a} * {b} = {multiplicacion(a,b)}")
elif operacion == "division":
    print(f"{a} % {b} = {division(a,b)}")
else:
    print("Operación no válida")