'''
Exemplo 02 - Maiusculas: 
  03 Variável -> texto, contador, texto_min
  04 Comandos -> print/ input/ count/ upper
'''

print('Digite um texto onde nele contenha a palavra "VIDA":')
texto = input()
texto_min = texto.upper()
contador = texto_min.count('VIDA')
print('A palavra "VIDA" está presente ', contador, 'X no texto digitado.')