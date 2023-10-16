while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*20)
    if num < 0:
        break
    for n in range(1,11):
        print(f'{num} X {n:2} = {num*n} ')
    print('-'*20)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
