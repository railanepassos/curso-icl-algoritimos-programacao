'''
  1 - Solicite ao Usuário escrever um pequeno texto contendo a palavra 'conhecimento'.
  2 - Calcule qts vezes a palavra 'conhecimento' apareceu no texto e informe na Tela o resultado.
'''

print("Digite um texto qualquer contendo a palabra 'conhecimento'")
texto = input()
quantidade_palavra = texto.count("conhecimento")
print("A palavra 'conhecimento' está presente ", quantidade_palavra, "vezes no texto digitado.")