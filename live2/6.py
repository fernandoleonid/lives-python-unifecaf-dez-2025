# Calular a média, onde a quantidade 
# de notas não padrão

nome = input ("Digite seu nome: ")
quantidade = int (input ("Digite a quantidade de notas: "))

total = 0
contador = 1
while (contador <= quantidade):
    nota = int (input(f"Digite sua nota {contador}: "))
    total += nota
    contador += 1

media = total / quantidade
print (f"{nome} sua média é: {media}")
