# 10.Número por extenso. Escreva um programa que solicite ao usuário a
# digitação de um número até 99 e imprima-o na tela por extenso.

num = input('Informe o número: ')

tamanho = len(num)
unidades = ['zero','um','dois','três','quatro','cinco','seis','sete','oito','nove']
nomes_estranhos = ['onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove']
dezenas_perfeitas = ['dez','vinte','trinta','quarenta','cinquenta','sessenta','oitenta','noventa']
teste_estranho = int(num)-10
if tamanho == 1:
    numero1 = unidades[int(num)]
    print(numero1)
elif int(num)%10 == 0:
    numero_dezena = dezenas_perfeitas[int(num[0])-1]
    print(numero_dezena)
elif teste_estranho <=9:
    numero_estranho = nomes_estranhos[int(num)-11]
    print(numero_estranho)
else:
    dig1 = int(num)/10
    dig2 = int(num)%10
    primeiro_digito = dezenas_perfeitas[int(dig1) -1]
    segundo_digito = unidades[dig2]
    print(f'{primeiro_digito} e {segundo_digito}')