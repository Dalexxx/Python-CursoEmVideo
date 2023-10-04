maior = 0
menor = 0
for p in range(1,6):
    peso = float(input(f'Peso da {p}° pessoa: '))
    if p == 1:
       maior = peso
       menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O menor peso é {menor}Kg')
print(f'O maior peso é {maior}Kg')





'''pesos = []
for c in range(1,6):
    peso = float(input(f'Peso da {c}° pessoa: '))
    pesos.append(peso)
maior_valor = max(pesos)
menor_valor = min(pesos)  
print(f'O maior peso lido foi de {maior_valor}Kg')
print(f'O menor peso lido foi de {menor_valor}Kg')'''


#leia 5 números /done
#guarde os números /done
#mostre o maior peso /done
#mostre o menor peso /done