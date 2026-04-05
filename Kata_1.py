# Problema 1: Achatar Lista Aninhada
# Implemente uma função recursiva flatten(lista) que receba uma lista que pode conter sublistas aninhadas em qualquer profundidade e retorne uma lista plana com todos os elementos na ordem original.

# Exemplos:
# flatten([1, [2, [3, 4], 5], 6])  # → [1, 2, 3, 4, 5, 6]
# flatten([[1, 2], [3, [4, [5]]]])  # → [1, 2, 3, 4, 5]
# Dica: Para verificar se um item é uma lista, use isinstance(item, list).

# Bordas Obrigatórias
# Seus testes devem cobrir pelo menos estas situações:

# Lista vazia []
# Lista sem nenhum aninhamento [1, 2, 3]
# Lista com sublistas vazias [[], [[], []], 1]
# Aninhamento muito profundo [[[[[1]]]]]
# Lista com apenas 1 elemento [42]
# Análise de Custo
# Responda: Qual é a complexidade de tempo e de espaço da sua solução? Use a notação 
# O.