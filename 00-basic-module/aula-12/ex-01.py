'''
1 - Solicite ao Usuário escrever uma palavra: Ex: Conhecimento
2 -  A partir da palavra escrita, imprima uma outra palavra Ex: cimento
'''

print('Digite uma Palavra: ')
palavra = input()
palavra_gerada = (palavra[5]+palavra[6]+palavra[7]+palavra[8]+palavra[9]+palavra[10]+palavra[11])
print('A palavra gerada é: ', palavra_gerada)