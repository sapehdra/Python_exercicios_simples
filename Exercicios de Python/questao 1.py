from statistics import mean

qtMercadoria = int(input('Insira a quantidade de mercadorias no estoque: '))
listaValores = []



for i in range(qtMercadoria):
    
    while qtMercadoria <= 0:
    	qtMercadoria = int(input('Por favor, insira um valor maior que ZERO!: '))
	valorMercadoria = float(input('Insira o valor da %dª mercadoria R$: ' %(i+1)))
	listaValores.append(valorMercadoria)

totalEstoque=sum(listaValores)

print('O valor total do estoque é de: R$ %.2f' %totalEstoque)

print('A média de valores do seu estoque é de: R$ %.2f' %mean(listaValores))
