nome = input('Informe o nome: ')
# nome = nome.upper()
# print(nome)
# nome = list(nome)
# nome_reverso = nome.sort(reverse = True)
# print(nome_reverso)
##########################
nome_lista = nome.upper().split()
nome_lista.reverse()
# ' '.join(nome_lista) #junta a lista com espaços em branco
print(' '.join(nome_lista))
