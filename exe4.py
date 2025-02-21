contagem_convidados = 0
resposta = 's'
while resposta.lower() == 's':  
    nome_convidado = input("insira o nome do convidado que deseja convidar para a festa: ")
    print("{} foi adicionado(a) com sucesso no convite!".format(nome_convidado))
    contagem_convidados += 1
    resposta = input("você quer convidar outra pessoa? (s/n): ")
print("\ntotal de convidados para a festa: {}".format(contagem_convidados))