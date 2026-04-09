cpf = int(input("Digite 9 dígitos do cpf: "))
quociente = cpf 

while quociente != 0: 
    digito = quociente % 10
    quociente = quociente // 10
    print(digito)

