import sys
import math

def menores(lista):
    lista1 = sorted(lista)
    print(lista1)
    

def distancia(vet1, vet2):
    resultado = 0
    i = 0
    
    
    
    for var in vet1:
        print(vet1[i])
        exit()
        resultado += pow(vet1[i] - vet2[i],2)
        i+=1
    
    return math.sqrt(resultado)

def converte(arquivo):

    
    classes = []
    
    for line in arquivo:
        auxiliar = line.split(',')
        i = 0
        
        linha = []
        for var in auxiliar:
            if ( auxiliar[i] != auxiliar[-1] ):
                linha.append(float(auxiliar[i]))
            else:
                linha.append(auxiliar[i].replace('\n', ''))
            i+=1

        classes.append(linha)
        
        #print(linha)
        #print('\n')
        
    return classes
    

def main():
    arq_base  = open('bases/train_59.data','r')
    arq_teste = open('bases/test_59.data','r')
    
    classesBase = converte(arq_base)
    classesTeste = converte(arq_teste)
    
    arq_base.close()
    arq_teste.close()
    
    for elementoTeste in classesTeste:
        for elementoBase in classesBase:
            distancia(elementoTeste, elementoBase)
    
    
if __name__ == '__main__':
    main()
    