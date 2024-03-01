# Programa para verificar si un prestamo puede ser consolidado segun el salario o deudas de las personas 

#entrada
Salario= int(input("cuanto es su salario : "))
Deuda= input("usted tiene otra deuda que no ha pagado (si o no) : ")

# Proceso salida
if Salario >= 945200:
    if Deuda == "no":
        print ("Su prestamo a sido aprobado")
    else:
        print ("Su prestamo a sido denegado")
else:
    print ("Su prestamo a sido denegado")

