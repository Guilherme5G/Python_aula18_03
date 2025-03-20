'''
idoso = input("Você é idoso?\n->")
cartao = input("Você tem o cartãozinho?\n->")

if idoso == "sim" and cartao == "sim":
    print("Pode estacionar👴")
else:
    print("Folgado pa carai")


idoso = input("Você é idoso?\n->")
deficiente = input("Você é deficiente?\n->")

if idoso == "sim" and deficiente == "sim":
    print("Pode estacionar👴")
else:
    print("Vaza safado🤬👊")'''

letra = input("Digite uma letra: ")

#Verificação de vogal
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Vogal")
else:
    print("Consoante")
