#- Crie uma variável chamada “adivinha” e defina o valor como 50. 
#Peça ao usuário para inserir um número. Embora o palpite não seja o mesmo que o valor do “adivinha”, diga a ele se o palpite é muito baixo ou muito alto e peça que ele dê outro palpite. 
#Se ele inserir o mesmo valor que “adivinha”, exiba a mensagem "Parabéns! Você acertou o número em {} tentativas!".

num = 50
tentativas = 0
palpite = int(input("Digite um número: "))
while palpite != num:
    if palpite < num:
        print("seu palpite é muito baixo! Tente novamente.")
    else:
        print("seu palpite é muito alto! Tente novamente.")
    tentativas += 1
    palpite = int(input("digite um número: "))
tentativas += 1 
print("parabéns! Você acertou o número em {} tentativas!".format(tentativas))
print("joao henrique")