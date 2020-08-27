# 9. Verificação de CPF. Desenvolva um programa que solicite a digitação de
# um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número
# válido ou inválido através da validação dos dígitos verificadores e dos
# caracteres de formatação.
#validando formato do cpf
def validar_formato_cpf(cpf):
    #xxx.xxx.xxx.-xx
    if cpf[3] != '.':
        return False
    elif cpf[7] != '.':
        return False
    elif cpf[11] != '-':
        return False
    return True

def validar_cpf(cpf):
    if validar_formato_cpf(cpf):
        cpf_limpo = cpf.replace('.','').replace('-','')
        contador = 10
        soma = 0
        for caractere in cpf_limpo:
            if contador >1:
                soma +=  int(caractere) * contador
                contador -=1

        digito1 = (soma * 10) % 11

        if digito1 == 10:
            digito1 = 0


        if digito1 != int(cpf_limpo[9]):
            return False

        contador = 11
        soma = 0
        for caractere in cpf_limpo:
            if contador >1:
                soma += int(caractere) * contador
                contador -=1
        digito2 = (soma * 10) % 11

        if digito2 == 10:
            digito2 = 0

        if digito2 != int(cpf_limpo[10]):
            return False
    else:
        return False

    return True

#teste
cpf = input('Informe o CPF válido: ')

if validar_cpf(cpf):
    print(f'{cpf}CPF VÁLIDO!')
else:
    print(f'{cpf}CPF INVÁLIDO!')







