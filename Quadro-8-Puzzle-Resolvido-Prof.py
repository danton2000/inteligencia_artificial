# Função que calcula a heurística simples de CONTAGEM de peças fora do lugar
def heuristica_simple(estado, estado_final):
    count = 0
    #Percorrendo  o tamanho de items que tem a lista(estado)
    for i in range(len(estado)):
        # i = index da lista(estado)
        if estado[i] != estado_final[i] and estado[i] != 0:
            # Contando quantos casos errados tem na lista(estado) com parando com a lista(estado_final)
            count += 1
    return count

# Função para obter os vizinhos possíveis de um estado dado
def pegar_vizinhos(estado):
    vizinhos = []
    #pegando o 0 da lista estado
    zero_index = estado.index(0)  # Encontra a posição do espaço vazio '0'

    if zero_index + 3 < 9:  # Mover o espaço para baixo
        vizinhos.append(troca_posicoes(estado, zero_index, zero_index + 3))
    if zero_index - 3 >= 0:  # Mover o espaço para cima
        vizinhos.append(troca_posicoes(estado, zero_index, zero_index - 3))
    if zero_index % 3 < 2:  # Mover o espaço para a direita
        vizinhos.append(troca_posicoes(estado, zero_index, zero_index + 1))
    if zero_index % 3 > 0:  # Mover o espaço para a esquerda
        vizinhos.append(troca_posicoes(estado, zero_index, zero_index - 1))

    return vizinhos

# Função para trocar duas posições em um estado e retornar o novo estado
def troca_posicoes(estado, i, j):
    novo_estado = list(estado)
    
    #trocando os valores de posição
    novo_estado[i], novo_estado[j] = novo_estado[j], novo_estado[i]
    
    return tuple(novo_estado)

# Algoritmo A* para encontrar a solução do quebra-cabeça
def a_estrela(estado_inicial, estado_final):
    conjunto_aberto = [(heuristica_simple(estado_inicial, estado_final), estado_inicial)]  # Lista de estados abertos
    
    # Preparando essas 2 varias com dicionario(chave(lista): valor)
    veio_de = {estado_inicial: None}
    g_pontuacao = {estado_inicial: 0}
    # print(conjunto_aberto)
    # Laco de repetição, só vai sair do laço quando ele resolver as peças erradas
    while conjunto_aberto:
        conjunto_aberto.sort(key=lambda x: x[0])  # Ordena pelo f_pontuacao

        atual = conjunto_aberto.pop(0)[1]  # Obtém o estado com menor f_pontuacao
        
        if atual == estado_final:
            return reconstruir_caminho(veio_de, estado_inicial, atual)  # Retorna o caminho até o estado final

        print(atual)
        
        for vizinho in pegar_vizinhos(atual):  # Para cada lista de vizinho do estado atual
            # Os vizinhos seriam as jogadas possiveis?
            
            """
            Para cada vizinho encontrado a partir do estado atual, 
            ele calcula uma "tentativa de pontuação g" que é a pontuação até o vizinho no momento. 
            Isso é feito somando a pontuação atual à distância entre o estado atual e o vizinho (que nesse caso é 1).
            """
            tentative_g_pontuacao = g_pontuacao[atual] + 1
            """
            Ele então verifica se o vizinho já foi mapeado na pontuação ou 
            se a nova pontuação é menor do que a pontuação já atribuída.
            """
            if vizinho not in g_pontuacao or tentative_g_pontuacao < g_pontuacao[vizinho]:
                """
                Em caso afirmativo, ele atualiza os valores: o estado anterior, 
                a distância e um epontuacao F que é a soma de G (distância) e 
                a heurística (distância estimada do vizinho ao estado final).
                """
                veio_de[vizinho] = atual
                g_pontuacao[vizinho] = tentative_g_pontuacao
                f_pontuacao = tentative_g_pontuacao + heuristica_simple(vizinho, estado_final)
                """
                Por fim, se passou nos critérios anteriores, ele adiciona o vizinho ao conjunto aberto 
                (conjunto de nós que ainda precisam ser verificados).
                """
                conjunto_aberto.append((f_pontuacao, vizinho))
    return []  # Retorna lista vazia se não encontrar solução

# Função para reconstruir o caminho da solução
def reconstruir_caminho(veio_de, start, estado_final):
    atual = estado_final
    path = []
    while atual != start:
        path.append(atual)
        atual = veio_de[atual]
    path.reverse()
    return path

# Estados inicial e final do quebra-cabeça
estado_inicial = (1, 0, 3, 4, 2, 5, 7, 8, 6)
estado_final = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Encontra o caminho para a solução do quebra-cabeça e imprime o caminho
caminho_solucao = a_estrela(estado_inicial, estado_final)
print(caminho_solucao)