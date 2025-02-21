#Faça um programa que peça o nome do convidado que o usuario deseja convidar para uma festa. Depois disso, exiba a mensagem "[nome] foi adicionado(a) com sucesso no convite!" e adicione 1 à contagem.
#Em seguida, pergunte se ele quer convidar outra pessoa.
#Continue repetindo isso até que ele não queira mais convidar ninguém para a festa e, em seguida, mostre quantas pessoas foram convidas para a festa.

contagem_convidados = 0
resposta = 's'
while resposta.lower() == 's':  
    nome_convidado = input("insira o nome do convidado que deseja convidar para a festa: ")
    print("{} foi adicionado(a) com sucesso no convite!".format(nome_convidado))
    contagem_convidados += 1
    resposta = input("você quer convidar outra pessoa? (s/n): ")
print("\ntotal de convidados para a festa: {}".format(contagem_convidados))
print("joao henrique")