def le_textos():
    ''' A função lê todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input(f'Digite o texto [{i}] (aperte Enter para sair): ').strip()
    while texto:
        textos.append(texto)
        i += 1
        texto = input(f'Digite o texto [{i}] (aperte Enter para sair): ').strip()
    
    return textos
txt = le_textos()
print(txt)
print(len(txt))