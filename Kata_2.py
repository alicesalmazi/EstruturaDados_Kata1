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