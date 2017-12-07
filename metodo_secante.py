def secante(f, x0, x1, epsilon, iterMax=50):
    """Executa o método da Secante para achar o zero de f  
       a partir das aproximações x0 e x1, e da tolerância 
       epsilon.
       Retorna uma tupla (houveErro, raiz), onde houveErro é booleano.
    """
    k = 0
    ## Teste se x0 e x1 já são raízes
    if(abs(f(x0)) < epsilon):
        return(False,x0)

    if(abs(f(x1)) < epsilon ):
        return(False,x1)
    
    ## Escreva o cabeçalho da tabela e as linhas para x0 e x1
    print("k\t x\t\t f(x)")
    print("%s\t%e\t%e" %("-",x0,f(x0)))
    print("%s\t%e\t%e" %("-",x1,f(x1)))
    ## Inicie as iterações (pode ser um for)
    for i in range(k,iterMax):
        if(f(x0) != f(x1)):
            x2 = (x1*f(x0) - x0*f(x1))/(f(x0)-f(x1)) # equação secante
            print("%d\t%e\t%e" % (k+1,x2,f(x2)))
            if(abs(f(x2)) < epsilon): # criterio de parada
                return (False,x2)
             
            x0 = x1
            x1 = x2
            k+=1
          
        else:
            print("divisão por zero")
            return (True,None)
    print("Numero maximo de interaçoes atingido.")
    return (True,x2)
