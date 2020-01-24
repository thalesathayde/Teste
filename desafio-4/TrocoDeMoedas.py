import sys

def troca(valor, moedas):
    aux=[]
    calcula=[]
    for i in range(valor+1):
        if i==0:
            aux.append(0)
        else:
            aux.append(sys.maxsize)
    for i in range(len(moedas)):
        calcula.append(aux.copy())
    #print(calcula)

    for i in range(len(moedas)):
        for j in range(valor+1):
            if(j >= moedas[i]):
                calcula[i][j]=min(calcula[i-1][j],1+calcula[i][j-moedas[i]])
            else:
                calcula[i][j]=calcula[i-1][j]
    #print(calcula)

    resp=[]
    if calcula[len(moedas)-1][valor]==sys.maxsize:
        return []
    else:
        i=len(moedas)-1
        j=valor
        resp=[]
        while(calcula[i][j]!=0):
            if calcula[i][j]==calcula[i-1][j] and i!=0:
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