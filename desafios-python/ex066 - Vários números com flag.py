tot = cont = 0
while True:
    num = int(input('Digite um valor (999 to stop): '))
    if num == 999:
        break
    tot += num
    cont += 1
    
print(f'A soma dos {cont} valores foi de {tot}!')