import datetime 
hoje = datetime.date.today()
 
nasc = input('Insira a data de nascimento do funcionário(DD/MM/AAAA):')
dataNasc = datetime.datetime.strptime(nasc, '%d/%m/%Y').date()
ingressoEmpresa = input('Insira a data de ingresso do funcionário(DD/MM/AAAA):')
dataEmpresa = datetime.datetime.strptime(ingressoEmpresa, '%d/%m/%Y').date()

def calculateAge(data): 
    diasAno = 365.2425   
    calcIdade = int((datetime.date.today() - data).days / diasAno) 
    return calcIdade 

idade = calculateAge(dataNasc)
tempoServico = calculateAge(dataEmpresa)

if ((idade >= 65) or (tempoServico >= 30) or ((idade >= 60) and (tempoServico >= 25))) :
    print('O funcionário possui %i anos e %i anos de casa, Ele pode requerer a aposentadoria' %(idade, tempoServico) ) 

else:
    print('O funcionário possui %i anos e %i anos de casa, Ele não pode requerer a aposentadoria' %(idade,tempoServico) )