salario = (float(input("Digite seu salário: ")))
if salario <= 1621:
    inss = salario * (7.5 /100)

if salario > 1621 and salario <= 2902.84:
    inss = 1621 *0.75 #(7.5%)
    inss = inss + (salario - 1621) * 0.09

if salario > 2902.84 and salario <= 4254.27:
    inss = 1621 * 0.075
    inss = inss + (2902.84 - 1621) * 0.09
    inss = inss + (salario - 4354.27) * 0.12

if salario > 4354.27 and salario <= 8475.55:
    inss = 1621 * 0.075
    inss = inss + (2902.84 - 1621) * 0.09
    inss = inss + (4354.27 - 2902.84) * 0.12
    inss = inss + (salario - 8475.55) * 0.14

if salario > 8475.55:
     inss = 1621 * 0.075
     inss = inss + (2902.84 - 1621) * 0.09
     inss = inss + (4354.27 - 2902.84) * 0.12
     inss = inss + (8475.55 - 4354.27) * 0.14

     print(f"Descono INSS é {inss}")
    

    