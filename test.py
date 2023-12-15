from random import randint
num = randint(0, 5)
count = 0
nome = str(input("Qual é o seu nome? "))
print(f'Muito prazer em te conhecer {nome}!')
print("Estou pensando em um número entre 0 e 5...")
print("Vamos jogar! Tente adivinhar em qual número estou pensando!")
x = int(input("Em qual número vc acha q estou pensando? "))
if x == num:
    count += 1
    print(f"Parabéns! Eu estava pensando em {num} mesmo!")
else:
    while (num != x):
        print("Tente Novamente!")
        count += 1
        x = int(input("Em qual número estou pensando? "))
        if x == num:
          print(f"Parabéns! Eu estava pensando em {num} mesmo!")
          print(f"Voce acertou depois de {count} tentativas")
