from statistics import mean

tempDias = []
mediaBaixa = 0 

for i in range(6):
    temp = float(input('Insira a temperatura média do %dº dia no vetor: ' %(i+1)))
    tempDias.append(temp)
for j in range(len(tempDias)):
    if tempDias[j] < (mean(tempDias)):
        mediaBaixa += 1
  
print('A temperatura mínima ente os 6 dias é de: %.1fº' %(min(tempDias)))
print('A temperatura mínima ente os 6 dias é de: %.1fº' %(max(tempDias)))
print('A média de temperatura ente os 6 dias é de: %.1fº' %(mean(tempDias)))

print('A temperatura ficou abaixo da média durante %d dias.' %mediaBaixa)