total = 0 
while total <= 50:  
    numero = int(input("Digite um número: ")) 
    total += numero  
    if total > 50:  
        print("O total é... {}".format(total))  
        break  