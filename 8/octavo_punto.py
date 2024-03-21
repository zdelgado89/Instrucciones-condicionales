# entrada
X = int(input("Digite un número: "))
Y = int(input("Digite un número: "))

# proceso
if X%Y == 0 or Y%X == 0:
    print("El número" , (X),  "es múltiplo de" , (Y))
else:
    print("El número" , (X), "no es múltiplo de" , (Y))