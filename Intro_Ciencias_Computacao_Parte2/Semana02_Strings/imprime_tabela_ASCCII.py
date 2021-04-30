'''
No ASCII (American Standard Code for Information Interchange),
cada caractere é representado usando apenas 7 bits, sendo que os c
aracteres de 0 a 31 são considerados de controle, e os de 32 a 127
correspondem aos caracteres comuns de um teclado de computador em inglês.
Execute o seguinte programa para ver os caracteres de 32 a 127:
'''

print("Tabela ASCII de 32 a 127: ")
for i in range(32, 128, 1):
    print("ASCII[ %3d ] = '%s'  |  ASCII[ %3d ] = '%s'  |  ASCII[ %3d ] = '%s'"%
    (i, chr(i), i+1, chr(i+1), i+2, chr(i+2)))
