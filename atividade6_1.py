print('Compara duas String')
texto1 = input('Informe o primeiro texto: ')
texto2 = input('Informe o segundo texto: ')
tamanho1 = len(texto1)
tamanho2 = len(texto2)
sao_iguais = texto1.lower() == texto2.lower()

def imprimir(texto1,texto2):
    print(f'String 1: {texto1}')
    print(f'String 2: {texto2}')
    print(f'tamanho de {texto1}: {tamanho1} caracteres')
    print(f'tamanho de {texto2}: {tamanho2} caracteres')
    if tamanho1 ==tamanho2:
        print('As duas strings possuem tamanhos iguais')
    else:
        print('As duas strings possuem tamanhos diferentes')
    if sao_iguais:
        print('As duas strings são iguais')
    else:
        print('As duas strings são diferentes')

imprimir(texto1,texto2)