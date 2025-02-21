soma = 0  
numero1 = float(input("digite o primeiro número: "))  
numero2 = float(input("digite o segundo número: "))  
soma = numero1 + numero2 
print("a soma dos numeros é", soma)
resp = input("você quer adicionar outro número? (sim/não): ").lower()
while  resp == "sim":
    num = float (input("digite o numero que deseja adicionar:"))
    soma += num
    resp = input("deseja adicionar esse numero a soma? ")
    print("a soma é", soma)
    print("joao henrique")
