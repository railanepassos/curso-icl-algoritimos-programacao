'''
Exemplo 01 - Contar palavras: 
  02 Variável -> texto, contador
  03 Comandos -> print/ input/ count
'''

print('Digite um texto onde nele contenha a palavra "vida":')
texto = input()
contador = texto.count('vida')
print('A palavra "vida"está presente ', contador, 'X no texto digitado.')