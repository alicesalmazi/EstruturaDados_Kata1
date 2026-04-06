# Problema 2: Busca Binária Recursiva (Sem Fatiamento)
# Implemente uma função recursiva binary_search(lista, alvo) que receba uma lista ordenada e um valor alvo, e retorne o índice do alvo na lista. Se o alvo não existir, retorne -1.

# ⚠️ Restrição: Você NÃO pode usar fatiamento (lista[:], lista[:meio], lista[meio:]). Use apenas índices.

# Por quê? Lembre-se da Aula 04: fatiamento copia dados na memória. Isso transforma uma busca eficiente em algo muito mais lento.

# Exemplos:
# binary_search([1, 3, 5, 7, 9, 11], 7)   # → 3
# binary_search([1, 3, 5, 7, 9, 11], 4)   # → -1
# Dica: Use parâmetros extras (inicio e fim) para controlar o intervalo de busca sem precisar fatiar.

# Bordas Obrigatórias
# Seus testes devem cobrir pelo menos estas situações:

# Lista vazia []
# Lista com 1 elemento (alvo existe e alvo não existe)
# Alvo é o primeiro elemento da lista
# Alvo é o último elemento da lista
# Alvo não existe (valor entre dois elementos da lista)

# Análise de Custo
# Responda:

# Qual é a complexidade de tempo da sua solução?
# Qual é a complexidade de espaço (pilha de chamadas)?
# O que aconteceria com a complexidade se você tivesse usado fatiamento em vez de índices?

class pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.array = [None] * capacidade
        self.top = -1
        
    def push(self, data):
        if self.topo == self.capacidade - 1:
            raise Exception("Stack Overflow")
        
        self.topo += 1
        self.array[self.topo] = data

    def pop(self):
        if self.topo == -1:
            raise Exception("Underflow")
        
        valor = self.array[self.topo]
        self.topo -= 1
        return valor

    def peek(self):
        return self.array[self.topo]
    
    def is_empty(self):
        return self.topo == -1

def binary_search(lista, alvo, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1

    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2

    if lista[meio] == alvo:
        return meio
    
    if lista[meio] < alvo:
        return binary_search(lista, alvo, meio + 1, fim)
    else:
        return binary_search(lista, alvo, inicio, meio - 1)
    

# Exemplos kata

P = pilha(6)
assert binary_search([1, 3, 5, 7, 9, 11], 7) == 3
P2 = pilha(6)
assert binary_search([1, 3, 5, 7, 9, 11], 4) == -1

# Edge Cases

# Lista Vazia []
P3 = pilha(6)
assert binary_search([], 3) == -1

# Lista com 1 elemento (alvo existe e alvo não existe)
P4 = pilha(6)
assert binary_search([1, 3, 5, 7, 9, 11], 9) == 4
p5 = pilha(6)
assert binary_search([1, 3, 5, 7, 9, 11], 13) == -1

# Alvo é o primeiro elemento da lista
P6 = pilha(6)
assert binary_search([1, 3, 5, 7, 9, 11], 1) == 0

# Alvo é o último elemento da lista
P7 = pilha(6)
assert binary_search([1, 3, 5, 7, 9, 11], 11) == 5

# Alvo não existe (valor entre dois elementos da lista)
P8 = pilha(6)
assert binary_search([1, 3, 5, 7, 9, 11], 2) == -1