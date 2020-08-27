

def nome_mes(mes):
    numero_mes = int(mes)
    if numero_mes < 1 or numero_mes > 12:
        return 'mês inválido'

    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jun',
             'jul','ago','set','out','nov''dez']
    return meses[numero_mes-1]

def eh_data_valida(data): #fazer as validações para as datas
    return True

data = (input('informe a data: '))

elementos_data = data.split('/')
print(f'Voce nasceu em {elementos_data[0]} de {nome_mes(elementos_data[1])} de {elementos_data[2]}')