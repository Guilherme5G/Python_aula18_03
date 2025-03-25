#Exercicio1

n1 = int(input("Digite um valor inicial: "))
n2 = int(input("Digite um segundo valor: "))

if n1 > n2:
    print(f"O maior numero é {n1:.2f}")
else:
    print(f"O mairo numero é {n2:.2f}")

#Exercicio2

anoNascimento = int(input("Digite seu ano de nascimento: "))
idade = 2025 - anoNascimento
if idade >= 16:
    print("Se dirija a uma urna para votação")
else:
    print("Você nao tem idade necessaria para votar")

#Exercicio3

senha = int(input("Digite sua senha: "))

if senha == 1234:
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")

#Exercicio4

macas = int(input("Quantas maçãs ira comprar: "))

if macas <= 12:
    valor = macas * 0.25
else:
    valor = macas * 0.30
print(f"O valor total da sua compra é {valor:.2f}")

#Exercicio5

valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite um segundo valor: "))
valor3 = int(input("Digite um terceiro valor: "))

if valor3 < valor2:
    valorAuxiliar = valor2
    valor2 = valor3
    valor3 = valorAuxiliar

if valor2 < valor1:
    valorAuxiliar = valor1
    valor1 = valor2
    valor2 = valorAuxiliar

if valor3 < valor2:
    valorAuxiliar = valor2
    valor2 = valor3
    valor3 = valorAuxiliar

print(f"A ordem crescente dos números é {valor1}, {valor2}, {valor3}")

#Exercicio6

altura = float(input("Insira sua altura em metros: "))
genero = input("Qual seu gênero: ")

if genero == "masculino":
    peso = (altura * 72.7) - 58
else:
    peso = (altura * 62.1) - 44.7

print(f"O seu peso ideal é {peso:.2f}")


#Exercicio7 e 8

numlados = int(input("Digite a quantidade de lados: "))
medidalados = int(input("Digite a medida dos lados: "))

if numlados <= 3:
    print("Não é um polígono")
if numlados == 3:
    print("Triângulo")
elif numlados == 4:
    print("Quadrado")
elif numlados == 5:
    print("Pentágono")
else:
    print("Poligono nao identificado")

print(f"O seu perimetro é {numlados * medidalados}")


#Exercicio9

valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite um segundo valor: "))
valor3 = int(input("Digite um terceiro valor: "))

maiorvalor = valor1

if valor2 > maiorvalor:
    maiorvalor = valor2
elif valor3 > maiorvalor:
    maiorvalor = valor3

print(f"O maior valor entre estes numeros é {maiorvalor}")

#Exercicio10

medidaLado1 = int(input("Qual o valor do lado 1: "))
medidaLado2 = int(input("Qual o valor do lado 2: "))
medidaLado3 = int(input("Qual o valor do lado 3: "))

if medidalados == 3:
    print("È um triangulo Equilátero")
elif medidalados == 2:
    print("È um triangulo Isóscele")
else:
    print("È um triangulo Escaleno")


#Exercicio11

ang1 = int(input("Qual o valor do primeiro ângulo: "))
ang2 = int(input("Qual o valor do segundo ângulo: "))
ang3 = int(input("Qual o valor do terceiro ângulo: "))

if ang1 == 90 or ang2 == 90 or ang3 == 90:
    print("È um triangulo Retângulo")
elif ang1 > 90 and ang2 > 90 and ang3 > 90:
    print("È um triangulo Obtusangulo")
else:
    print("È um triangulo Acutângulo")

