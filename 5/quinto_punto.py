# Un programa para calcular el costo de agua por m3 

# Input

M3 = int(input("cuanta agua gasto este mes?: "))
cuota_fija= 10000
# Processing

if M3 < 50:
    PAGO = 0 + cuota_fija
elif M3 < 200:
    PAGO = ((M3-50) *2000) +cuota_fija
else:
    PAGO = ((M3-50) *3000) +cuota_fija

# Output 

print ("El dinero a pagar por el gasto del agua es: ",PAGO,)