## Comando UPPER - Converte para maiúsculas
nome = "lucas"
print(nome.upper())

## Comando LOWER - Converte para minúsculas
nome = "LUCAS"
print(nome.lower())

## Comando CAPITALIZE - Converte a primeira letra para maiúscula
nome = "lucas"
print(nome.capitalize())

## Comando TITLE - Converte a primeira letra de cada palavra para maiúscula e as demais para minúsculas
nome = "lucas"
print(nome.title())

## Comando FIND - Encontra a primeira ocorrência de um caractere ou substring
nome = "lucas"
print(nome.find("a"))

## Comando REPLACE - Substitui um caractere ou substring por outro
nome = "lucas"
print(nome.replace("a", "o"))

## Commando Strip - Remove espaços em branco do início e do fim da string
nome = "  lucas  "
print(nome.strip())

## Comando LStrip - Remove espaços em branco do início da string
nome = "  lucas  "
print(nome.lstrip())

## Comando RStrip - Remove espaços em branco do fim da string
nome = "  lucas  "
print(nome.rstrip())

## Comando Split - Divide a string em uma lista de sub-strings baseado em um caractere ou substring
nome = "lucas,joão,maria"   #baseado em uma vírgula como separador
print(nome.split(","))

## Commando Join - Junta uma lista de sub-strings em uma string baseado em um caractere ou substring
nome = ["lucas", "joão", "maria"]   #baseado em uma vírgula como separador como o split acima
print(",".join(nome))

## Comando Len - Retorna o número de caracteres da string
nome = "lucas"
print(len(nome))

## Comando Count - Retorna o número de ocorrências de um caractere ou substring
nome = "lucas"
print(nome.count("a"))

## Comando Index - Retorna o índice da primeira ocorrência de um caractere ou substring
nome = "lucas"
print(nome.index("a"))
