from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
fim = True
while fim:
    print('=-'*15)
    print('[ 1 ] somar')
    print('[ 2 ] multiplar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    c = int(input('>>>>>Qual é a sua opção? '))
    if c == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} + {num2} é {soma}')
    elif c == 2:
        mult = num1 * num2
        print(f'A multiplicação entre {num1} x {num2} é {mult}')
    elif c == 3:
        if num1 > num2:
            print(f'Entre {num1} e {num2} o maior valor é o {num1}')
        else:
            print(f'Entre {num1} e {num2} o maior valor é o {num2}')
    elif c == 4:
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif c == 5:
        print('Finalizando...')
        sleep(2)
        fim = False
    else:
        print('Opção inválida. Tente novamente')
print('Saiu do programa!')