import math

numero = float(input("num: "))

if numero >= 0:
    raiz = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é igual a {raiz}!")
else:
    print("Impossiviel extrair raiz de número negativo!")
    
