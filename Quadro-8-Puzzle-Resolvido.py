# Fonte do código: https://github.com/talesconrado/8-puzzle_bfs-astar/tree/master

tabuleiro = str(
    [
        [1,0,3],
        [4,2,5],
        [7,8,6]
    ]
)

obj_final = str(
    [
        [1,2,3],
        [4,5,6],
        [7,8,0]
    ]
)

def move(tab_original):
    """
    Checa possíveis movimentos (os nós)
    da árvore
    """
    movimentos = []
    #eval = permite avaliar expressões matemáticas ou trechos de código Python presentes em forma de strings.
    tab = eval(tab_original)
    print(tab)
    i = 0
    j = 0
    print(tab[i])
    # Encontrnado o 0, caso não encontre o i é imcremetnado
    
    while 0 not in tab[i]: i += 1
    j = tab[i].index(0)
    print(tab[i])
    #print(tab [j])
    #print(tab[i][j])
    if i<2:         
        #mover o 0 para baixo 
        print("Incio Inverter")
        print(tab[i][j])
        print(tab[i+1][j])
        print(tab[i+1][j])
        print(tab[i][j])
        print("Fim Inverter")
        tab[i][j], tab[i+1][j] = tab[i+1][j], tab[i][j]
        print(tab[i]) 
        print(tab[i][j])
        quit()
        movimentos.append(str(tab))
        tab[i][j], tab[i+1][j] = tab[i+1][j], tab[i][j]

    if i>0:         
        #mover o 0 para cima
        tab[i][j], tab[i-1][j] = tab[i-1][j], tab[i][j]  
        movimentos.append(str(tab))
        tab[i][j], tab[i-1][j] = tab[i-1][j], tab[i][j]  

    if j<2:         
        #mover o 0 para a direita
        tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j]
    
    if j>0:         
        #mover o 0 para a esquerda
        tab[i][j], tab[i][j-1] = tab[i][j-1], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i][j-1] = tab[i][j-1], tab[i][j]

    return movimentos

def buscaLargura(start,end):
    """
    Usa busca em largura para 
    resolver o quebra-cabeça
    """
    explorado = []
    banco = [[start]]
    while banco:
        i = 0
        caminho = banco[i]
        banco = banco[:i] + banco[i+1:]
        final = caminho[-1]
        print(final)
        if final in explorado: 
            continue
        for movimento in move(final):
            if movimento in explorado:
                continue
            banco.append(caminho + [movimento])
        explorado.append(final)
        if final == end: break
    return caminho

print("Usando Busca em Largura:")
for tabuleiro in buscaLargura(tabuleiro,obj_final):
    print("Movimentos Possiveis")
    print(tabuleiro, end="\n")