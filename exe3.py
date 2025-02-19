soma = 0  
continuar = 'sim'  

while continuar == 'sim':  
    numero1 = int(input("digite o primeiro número: "))  
    numero2 = int(input("digite o segundo número: "))  
    soma += numero1 + numero2  
    continuar = input("você quer adicionar outro número? (sim/não): ").lower()
print("a soma total é:", soma)  