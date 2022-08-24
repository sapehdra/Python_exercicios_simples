listaNomes = []

for i in range(5):
    nomes = str(input('Insira o nome da %dª pessoa: ' %(i+1)))
    listaNomes.append(nomes.upper())
buscaNomes = str(input('Insira o nome da pessoa a ser procurada na lista: '))
capNomes = buscaNomes.upper()

if capNomes in listaNomes:
    print('Achei')
else:
    print('Não achei')
