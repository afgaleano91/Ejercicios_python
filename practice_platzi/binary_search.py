target = int(input("ingresa un numero: "))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, target)
response = (alto + bajo) / 2

while abs(response**2 - target) >= epsilon:
    if response**2 < target:
        bajo = response
    else:
        alto = response

    response = (alto + bajo) / 2

print(f'la raiz cuadrada de {target} es {response}')
