#Exercicio1 (correto)

n1 = int(input("Digite um valor inicial: "))
n2 = int(input("Digite um segundo valor: "))

if n1 > n2:
    print(f"O maior numero é {n1:.2f}")
else:
    print(f"O mairo numero é {n2:.2f}")

#Exercicio2 (corrigido)

anoNascimento = int(input("Digite seu ano de nascimento: "))
idade = 2025 - anoNascimento
if idade < 16:
    print("Proibido votar")
elif idade < 18 or idade >= 70:
    print("Você pode votar, mas sem obrigatoriedade")
else:
    print("Votar é obrigatório")

if idade < 16:
    print("Proibido votar")
elif idade < 18:
    print("Você pode votar, mas sem obrigatoriedade")
elif idade < 70:
    print("Votar é obrigatório")
else:
    print("Votar é opcional,velho imundo")

#Exercicio3 (corrigido)
senha_fornecida = 1234
senha = input("Digite sua senha:\n-> ")

if senha == senha_fornecida:
    print("ACESSO LIBERADO")
else:
    print("ACESSO NEGADO")

#Exercicio4 (corrigido)

#macas = int(input("Quantas maçãs ira comprar: "))

#if macas < 12:
    #valor = macas * 0.30
#else:
   #valor = macas * 0.25
#print(f"O valor total da sua compra é {valor:.2f}")

quantidade = int(input("Diga a quantidade de maçãs: "))
valor = 0.25
if quantidade < 12:
    valor = 0.3
total = quantidade*valor
print(f"Você gastará R${valor: .2f} em {quantidade} maçãs, à R${valor} por maçã.")

'''
#Exercicio5 (correto, porém analisar)

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

#segunda forma de fazer a 5
maior = valor1
if valor2 > maior:
    maior = valor2
if valor3 > maior:
    maior = valor3 
    
menor = valor1
if valor2 < menor:
    menor = valor2 
if valor3 < menor:
    menor = valor3 
meio = valor1 + valor2 + valor3 - menor - maior
print(a, b, c)

#Exercicio6 ( corrigido )

altura = float(input("Insira sua altura em metros: "))
genero = input("Qual seu gênero: ")

if genero == "masculino":
    peso = (altura * 72.7) - 58
else:
    peso = (altura * 62.1) - 44.7
print(f"O seu peso ideal é {peso:.2f}")

altura = float(input("Insira sua altura em metros: "))
genero = input("Qual seu gênero: ")
peso = (altura * 62.1) - 44.7
if genero == "masculino":
    peso = (altura * 72.7) - 58
print(f"O seu peso ideal é {peso:.2f}")


#Exercicio7 e 8 (super corrigido!!!)

numlados = int(input("Digite a quantidade de lados:\n->"))
if numlados < 3:
    print("Não é um polígono")
elif numlados > 5:
    print("Polígono nao identificado")
else:
    medidalados = int(input("Digite a medida dos lados:\n->"))
    perimetro = numlados*medidalados
    if numlados == 3:
        forma = "Triangulo"
    elif numlados == 4:
        forma = "Quadrado"
    else:
        forma = "Pentágono"
    print(f"É um {forma} de perímetro {perimetro}")


#Exercicio9 (Correto)
valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite um segundo valor: "))
valor3 = int(input("Digite um terceiro valor: "))

maiorvalor = valor1

if valor2 > maiorvalor:
    maiorvalor = valor2
if valor3 > maiorvalor:
    maiorvalor = valor3

print(f"O maior valor entre estes numeros é {maiorvalor}")

#Exercicio10 ( corrigido )

a = int(input("Qual o valor do lado 1: "))
b = int(input("Qual o valor do lado 2: "))
c = int(input("Qual o valor do lado 3: "))

if a == b and a == c:
    print("Equilatero")
elif a == b or a == c or c == b:
    print("Isósceles")
else:
    print("Escaleno")

#Exercicio11 (corrigida)

ang1 = int(input("Qual o valor do primeiro ângulo: "))
ang2 = int(input("Qual o valor do segundo ângulo: "))
ang3 = int(input("Qual o valor do terceiro ângulo: "))
if a+b+c == 180:
    if ang1 == 90 or ang2 == 90 or ang3 == 90:
        print("È um triangulo Retângulo")
    elif ang1 > 90 and ang2 > 90 and ang3 > 90:
        print("È um triangulo Obtusangulo")
    else:
        print("È um triangulo Acutângulo")
else:
    print("Não é um triangulo")
'''
