'''
Exemplo 02 - Minúsculas: 
  03 Variável -> texto, contador, texto_min
  04 Comandos -> print/ input/ count/ lower
'''

print('Digite um texto onde nele contenha a palavra "vida":')
texto = input()
texto_min = texto.lower()
contador = texto_min.count('vida')
print('A palavra "vida" está presente ', contador, 'X no texto digitado.')