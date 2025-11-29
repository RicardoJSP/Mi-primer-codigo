# HOLA GIT

print("Resolviendo la ecuacion x= -b + b^2 - a*c* (4*a+b) - a^2")

# A diferencia de PHP, las variables se definen sin un "$"
a = 2
b = 3
c = 4

# Siguiendo el orden jerarquico, resolvemos el parentesis primero:
parentesis = 4 * a + b
print("El resultado del paréntesis es: ", parentesis)

# Resolvemos las potencias:
potencia1 = b ** 2
potencia2 = a ** 2
print("El valor de la potencia 1 (b^2) es: ", potencia1)
print("El valor de la potencia 2 (a^2) es: ", potencia2)

# Resolvemos la multiplicacion
multiplicacion = a * c * parentesis
print("El valor de la multiplicacion es: ", multiplicacion)

# Paso final, pasamos en limpio a la ecuacion:
x = -b + potencia1 - multiplicacion - potencia2
print("El resultado de la ecuacion es: ", x)


print("asdasdasda")
