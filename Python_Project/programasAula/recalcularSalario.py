salario = float(input("Digite o seu salário: "))

if salario <= 1903.98:
    aliquota = 0
elif salario <= 2826.65:
    aliquota = 0.075
elif salario <= 3751.05:
    aliquota = 0.15
elif salario <= 4664.68:
    aliquota = 0.225
else:
    aliquota = 0.275

desconto = salario*aliquota
salarioNovo = salario - desconto
print(f"O salário recalculado é R${desconto:.2f} e você receberá R${salarioNovo:.2f} ")

