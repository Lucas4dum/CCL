import matplotlib.pyplot as plt
def inserirndoXY():
    vetorx=[]
    vetory=[]
    matrizXY=[]
    vetorTotais=[] 
    i=0
    boolVariavel=True
    while boolVariavel==True:
        variavel=input("Digite um valor ")
        boolVariavel=variavel.isnumeric()
        if variavel.isnumeric():
            print(i)
            if i % 2 == 0:
                vetorx.append(float(variavel))
                print("X",variavel)
            else:
                vetory.append(float(variavel))
                print("Y",variavel)
        elif i % 2 != 0:
           vetorx.pop(len(vetorx)-1)
        i+=1       
    matrizXY.append(vetorx)
    matrizXY.append(vetory)    
    valorN=len(vetorx)
    for i in range(3):
        vetor=[]
        for j in range(valorN):
            if i < 2:
                vetor.append(matrizXY[i][j]**2)
            else:
                vetor.append(matrizXY[0][j]*matrizXY[1][j])
        matrizXY.insert(i+2, vetor) 
    for i in range(5):
        vetorTotais.append(sum(matrizXY[i]))
    exibir(matrizXY, vetorTotais)
    return matrizXY, vetorTotais, valorN

def exibir(matrizXY, vetorTotais):
    print('{:^15} {:^15} {:^15} {:^15} {:^15}'.format("X","Y","X^2","Y^2","XY"))
    for j in range(len(matrizXY[0])):        
        for i in range(5):
            print('{:^15}'.format(matrizXY[i][j]),end='')
        print()    
    for i in range(5):
            print('{:^15}'.format(vetorTotais[i]),end='')
    print("Totais")
    
def coeficienteDeCorrelacao(vetorTotais,valorN,matrizXY):
    dividendo=valorN*vetorTotais[4]-vetorTotais[0]*vetorTotais[1]
    diferencaTotalX=valorN*vetorTotais[2]-vetorTotais[0]**2
    diferencaTotalY=valorN*vetorTotais[3]-vetorTotais[1]**2
    divisor=(diferencaTotalX**0.5)*(diferencaTotalY**0.5)
    rxy = dividendo/divisor   
    return rxy, regressaoLinear(dividendo, diferencaTotalX, vetorTotais,valorN, matrizXY)

def regressaoLinear(dividendo, diferencaTotalX, vetorTotais,valorN, matrizXY):
    reta=[]
    coefAngular=dividendo/diferencaTotalX
    intercepto=vetorTotais[1]/valorN-coefAngular*(vetorTotais[0]/valorN)    
    for i in range(valorN):
        reta.append(round(intercepto+coefAngular*matrizXY[0][i],3))
    print("Y=",intercepto,"+",coefAngular,"X")
    return reta

matrizXY, vetorTotais, valorN = inserirndoXY()
rxy, reta = coeficienteDeCorrelacao(vetorTotais, valorN, matrizXY)
print("COEFICIENTE DE CORRELAÇÃO LINEAR ",rxy,"\n",reta)
fig, ax = plt.subplots()
ax.set_xlabel(input("Digite qual será o texto em X: "))
ax.set_ylabel(input("Digite qual será o texto em Y: "))
retaRegressao,=ax.plot(matrizXY[0],reta, label="Reta da regressão linear")
ax.set_title("Reta da Regressão Linear")
ax.scatter(matrizXY[0],matrizXY[1])
plt.show()