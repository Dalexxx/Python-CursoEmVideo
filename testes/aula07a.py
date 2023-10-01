n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2

print(f'A soma é {s}, a divisão é {d:.2f} e a multiplicação é {m}', end=' ')
print(f'o resto da divisão é {di} e a potenciação é {p}')