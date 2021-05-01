'''print('='*50)
x = 1
cont = 0
while x < 3:
    y = 0
    while y <= 4:
        print(y)
        y = y + 1
    x = x + 1

print('='*50)
cont = 0
fora = 5
while fora > 0:
  dentro = 0
  while dentro < fora:
    print("oi")
    cont += 1
    dentro = dentro + 1
  fora = fora - 1
print(cont)
print('='*50)


def tabuada():
    tab = 1
    while tab <= 10:
        print("Tabuada do", tab, ":", end="\t")
        i = 1
        print(tab*i, end = "\t")
        i = i + 1
        print()
        tab = tab + 1
tabuada()

print('='*50)
x = 2
cont = 0
while x >= 0:
    y = 0
    while y >= 4:
        print(y)
        y = y + 1
    x = x - 1
print('='*50)



print('='*50)

i = 0
while i < 3:
  j = 0
  while j < 3:
    print(3*i+j+1, end=' ')
    j = j + 1
  i = i + 1
'''

x = 1
while x < 3:
    y = 1
    while y < 3:
        print(x*y, end = "\t")
        y = y + 1
    x = x + 1
