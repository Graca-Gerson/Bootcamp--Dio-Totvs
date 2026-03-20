## Interpolando com % - OBS: O % é um placeholder para uma variável
nome = "Lucas"
idade = 25
print("Nome: %s, Idade: %d" % (nome, idade))

## Interpolando com f-string - OBS: O f é um placeholder para uma variável
nome = "Lucas"
idade = 25
print(f"Nome: {nome}, Idade: {idade}")

## Interpolando com format - OBS: O format é um placeholder para uma variável
nome = "Lucas"
idade = 25
print("Nome: {}, Idade: {}".format(nome, idade))

PI = 3.14159
print(f"Valor dePI: {PI:.2f}")

print("PI: {:.2f}".format(PI))

print(f"Valor de PI: {PI:10.2f}")
