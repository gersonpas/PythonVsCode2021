num = int(input('Entre com um número: '))
u = num //  1 % 10
d = num //  10 % 10
c = num //  100 % 10
m = num //  1000 % 10
print('Analizando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

n = str(input('Entre com o nome completo: ')).split()# ou strip()
#nome = n.split() # se usar strip() na linha 01 é necessário a linha 02.
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é: {} '.format(n[0]))
print('Seu último nome é: {}'.format(n[len(n)-1]))
