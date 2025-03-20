salario = float(input("Digite o seu salário: "))

if salario <= 1903.98:
    print("Seu salário continua o mesmo")
elif salario >= 1903.99 and salario <= 2826.65:
    salarioNovo = salario - (salario * 0.075)
    print(f"O salário recalculado é R${salarioNovo}")
elif salario >= 2826.66 and salario <= 3751.05:
    salarioNovo = salario - (salario * 0.15)
    print(f"O salário recalculado é R${salarioNovo}")
elif salario >= 3751.06 and salario <= 4664.68:
    salarioNovo = salario - (salario * 0.225)
    print(f"O salário recalculado é R${salarioNovo}")
elif salario >= 4664.69:
    salarioNovo = salario - (salario * 0.275)
    print(f"O salário recalculado é R${salarioNovo}")