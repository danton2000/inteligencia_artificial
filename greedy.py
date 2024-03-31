# Representação das conexões entre cidade
# Dicionário em Python? {}
# Listas em Python? []
# Tupla em Python? (cidade, distancia)
conexoes = {
    'A': [('C', 2), ('D', 3)],
    'C': [('D', 1), ('E', 4), ('F', 6)],
    'D': [('E', 1), ('G', 5)],
    'E': [('B', 5), ('F',2)],
    'F': [('B', 3)],
    'G': [('E', 2), ('B', 9)],
    'H': [('A', 4), ('D', 3)],
    'I': [('H', 3), ('J', 6)],
    'J': [('A', 5)],
    # adicionar quantas cidades e conexões quiser
}

# Heurística para a distância de 'x' Até cidade B
heuristica = {
    'A': 7, 'C': 5, 'D': 7, 'E': 3, 'F': 2,
    'G': 6, 'H': 8, 'I': 9, 'J': 10, 'B': 0
}

def busca_greedy(origem, destino):
    # Inicializar a fronteira (cidades adjacentes) a partir da cidade origem
    fronteira = [(origem, 0)] # lista de tuplas
    visitados = set() # set? conjunto de itens únicos| cidades visitadas
    
    # Laço
    while fronteira:
        # Escolhe a cidade com a menor heuristica na fronteira
        atual, _ = min(fronteira, key=lambda x: heuristica[x[0]]) # Busca Gulosa
        fronteira = list(filter(lambda x: x[0] != atual, fronteira)) # Remove a cidade atual
        
        print(f"Visitando: {atual}")
        
        if atual == destino:
            print("Destino Encontrado")
            return
        
        visitados.add(atual)
        # Adiciona as cidades conectadas à fronteira, se não foram visitadas
        for vizinho, distancia in conexoes.get(atual, []):
            if vizinho not in visitados:
                fronteira.append((vizinho, distancia)) # adiciona um tupla a fronteira

busca_greedy('A', 'B')

# Para a forma de estrela preciso somer os CUSTOS ...