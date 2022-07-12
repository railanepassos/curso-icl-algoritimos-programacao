
print("Digite um Testo Simples: ")
texto_original = input()
print("Digite palavra que deseja substituir no texto: ")
palavra_substituir = input()
print("Digite palavra substituta: ")
palavra_substituta = input()
texto_modificado = texto_original.replace(palavra_substituir, palavra_substituta)
print("Esse é seu novo texto após alterações: \n ", texto_modificado)