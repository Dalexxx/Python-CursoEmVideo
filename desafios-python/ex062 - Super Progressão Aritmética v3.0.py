print('Gerador de PA')
print('-=' * 10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 0
tot = 0
while cont is not 11:
    print(f' {termo} >', end='')
    termo += razao
    cont += 1
    if cont is 11:
        print(' PAUSA')
        pausa = int(input('Quantos termos você quer mostrar a mais?'))
        cont -= pausa
    tot += 1
print(f' Progressão finalizada com {tot} termos mostrados.')