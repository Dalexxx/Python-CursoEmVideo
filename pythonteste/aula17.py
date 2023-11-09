num = [2, 5, 9, 1]
num[2] = 3
num.append(7) #adiciona um valor a lista
num.sort(reverse=True) #sort : organiza reverse=True Coloca de trás pra frente
num.insert(2, 0) #adiciona o valor 0 na posição 2
num.remove(2) #ele elimina o primeiro valor que vc mandou eliminar
num.pop() #elimina o ultimo valor se n declarar a posição
print(num)
print(f'Essa lista tem {len(num)} elementos.')

a = [2, 3, 4, 7]
#b = a #faz uma ligação entre b e a, se alterar o b altera o a tbm
b = a[:] #recebe os valores de a e faz uma cópia
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista b: {b}')