
resultado=[]
def OrdenarResultado(lista) :
    for x in range(len(lista)) :
        for j in range(x+1,len(lista)):
            if lista [x]>lista[j]:
                tmp= lista[x]
                lista [x]= lista[j]
                lista [j]= tmp
    resultado = lista
    return resultado

    

