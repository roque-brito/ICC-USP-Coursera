# fatiar listas
# --------------------
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print('='*100)
print(primos)
print('Comprimento da lista = ', len(primos))
print('='*100)
# --------------------------------------------------------------------------------------------------------
print(primos[:12]) # imprime a lista do começo até a posição 12 (12° elemento)
# --------------------------------------------------------------------------------------------------------
print(primos[12:]) # imprime a lista do 12° elemento até o final
# --------------------------------------------------------------------------------------------------------
fatia = primos[5:20] # extrai um pedaço da lista
print(fatia)
# --------------------------------------------------------------------------------------------------------
inverte = primos[::-1] # inverte a ordem da lista: (:) = do começo; (:) = ao fim; (-1) = começando pelo último ítem
print(inverte)
# --------------------------------------------------------------------------------------------------------
# máximo // minimo // soma termos de uma lista
minimo = min(primos)
print(minimo)
maximo = max(primos)
print(maximo)
soma = sum(primos)
print(soma)