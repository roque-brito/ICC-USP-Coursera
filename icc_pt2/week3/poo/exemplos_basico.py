class Carro:
    pass # classe vazia

# cria uma instância "meu_carro":
meu_carro = Carro()
print(meu_carro) # nome da instancia __main__, junto com o endereço na memória

# podes criar outra instância:
carro_ime = Carro()
print(carro_ime) # observar o endereço diferente na memoria

# criar atributos ao objeto (instanciado):
meu_carro.ano = 2019
meu_carro.modelo = 'Prisma'
meu_carro.cor = 'Branco'
print(meu_carro.ano, meu_carro.modelo, meu_carro.cor)

carro_ime.ano = 1999
carro_ime.modelo = 'Saveiro'
carro_ime.cor = 'Verde'
print(carro_ime.ano, carro_ime.modelo, carro_ime.cor)

# manipulação de atributos e objetos instanciados:

novo_carro = meu_carro
novo_carro.ano += 2
print(meu_carro.ano)



