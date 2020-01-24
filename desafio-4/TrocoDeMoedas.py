import sys

def troca(valor, moedas):

    #criacao de uma matriz Valor+1 por Moedas Diferentes, onde a primeira coluna eh composta de zeros e o resto eh um valor muito alto
    aux=[]
    calcula=[]
    for i in range(valor+1):
        if i==0:
            aux.append(0)
        else:
            aux.append(sys.maxsize)
    for i in range(len(moedas)):
        calcula.append(aux.copy())


    #comecando da moeda mais baixa a mais alta calcula a quantidade minima de moedas, contando com as anteriores,
    #necessaria para chegar ao valor do indice j.
    for i in range(len(moedas)):
        for j in range(valor+1):
            if(j >= moedas[i]):
                #pega a menor quantidade de moedas necessarias entre o resultado obtido para a moeda anterior,
                #ou o resultado dessa moeda mais as moedas usadas anteriormente.
                calcula[i][j]=min(calcula[i-1][j],1+calcula[i][j-moedas[i]])
            else:
                calcula[i][j]=calcula[i-1][j]


    #pega a matriz anterior onde calcula[len(moedas)-1][valor] eh o menor numero de moedas
    #necessarias para fazer o troco e transforma em quais moedas foram usadas
    resp=[]
    if calcula[len(moedas)-1][valor]==sys.maxsize:
        #se entrou nesse if, significa que nao existe combinacao possivel
        return []
    else:
        i=len(moedas)-1
        j=valor
        resp=[]
        while(calcula[i][j]!=0):
            #se o resultado para esse j for igual o resultado da moeda anterior,
            #isso significa que nao foi essa moeda que foi usada, entao passa para a moeda anterior
            #se nao for igual, entao foi essa a moeda usada.
            if calcula[i][j]==calcula[i-1][j] and i!=0:
                #o teste do i!=0 eh porque, se nao me engano, toda lista em python eh ciclica
                i=i-1
            else:
                resp.append(moedas[i])
                j=j-moedas[i]
    

    #muda a formatacao para a saida pedida
    qtd=0
    num=0
    respFormatada=[]
    for i in range(len(resp)):
        if num!=resp[i]:
            if num!=0:
                respFormatada.append((qtd,num))
            num=resp[i]
            qtd=1
        else:
            qtd=qtd+1
    respFormatada.append((qtd,num))

    return respFormatada


print(troca(17, [1, 5, 10, 25, 50, 100]))
print(troca(14, [1, 7, 10]))
print(troca(10, [2, 3]))
print(troca(17, [2]))

#troca(17, [1, 5, 10, 25, 50, 100]) = [(1, 10), (1, 5), (2, 1)]
#troca(14, [1, 7, 10]) = [(2, 7)]
#troca(10, [2, 3]) = [(2, 3), (2, 2)]
#troca(17, [2]) = []