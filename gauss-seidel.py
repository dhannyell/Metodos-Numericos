def norma(v,x):
    """Calcula a norma entre dois vetores v e x.
    """
    r=[]
    # ESCREVA SEU CODIGO AQUI
    for i in range(0,len(v)):
        r.append(0)  # criando uma lista do tamanho de v iniciada em 0
        r[i] = v[i] - x[i] #armazenando o valor x(k+1) - x(k) em r
        a = [abs(x) for x in r] # modulo da lista r
    b = [abs(x) for x in v] # modulo da lista v(k+1)
    #uniques = [i for i in a if a.count(i) < 2] # verificando se existe elementos repetidos em r
    #uniques2 = [i for i in b if b.count(i) < 2] # verificando se existe elementos repetidos em v
    max_value = max(a) # pegando o maior valor de r
    max_value2 = max(b) # pegando o maior valor de v
    rn = max_value/max_value2 # resultado da norma
    return rn
    
    def seidel(A, b, epsilon, iterMax=50):
    """Resolve o sistema linear Ax=b usando o método iterativo Gauss-Seidel.
    O critério de parada utiliza a norma-infinito.
    Saída é o vetor x.
    
    """
    # ESCREVA SEU CODIGO AQUI  
    n = len(A)
    x = [0 for i in range(n)] #inicia o vetor com n elementos
    v = [0 for i in range(n)] #inicia o vetor com n elementos
    tem = [0 for i in range(n)] #inicia o vetor com n elementos
    #x = v[:]
    contador = 0
    
    for i in range(0,n):
        if A[i][i] !=0:
            for j in range(0,n):
                if i!= j:
                    A[i][j] = A[i][j]/A[i][i] #divide os elementos da matriz pelos pivo
            b[i] = b[i]/A[i][i] # divide o vetor solução pelo pivo
            A[i][i] = 0.0
    
    
    while contador < iterMax:         
        for i in range(0,n):
            tem[i]=sum([A[i][j]*v[j] for j in range(0,n) if i != j])
            #print(tem)
            v[i] = (b[i] - tem[i]) #x(k+1) = vetor solução - (elementos da matriz * x(k))
            #print(v)
        if norma(v, x) < epsilon:
            return v
        
        x = v[:]
        contador = contador+1
    print("Quantidade de interações insuficiente para encontrar o valor")
    return x
