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
# Responda: Qual é a complexidade de tempo e de espaço da sua solução? Use a notação O.

# Pilha Array
class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.array = [None] * capacidade
        self.topo = -1

    def push(self, dado):
        if self.topo == self.capacidade - 1:
            raise Exception("Stack Overflow")

        self.topo += 1

        self.array[self.topo] = dado

    def pop(self):
        if self.topo == -1:
            raise Exception("Undeflow")

        valor = self.array[self.topo]
        self.topo -= 1
        return valor
    
    def peek(self):
        return self.array[self.topo]

    def is_empty(self):
        return self.topo == -1

    def listaPilha(self):
        return self.array[:self.topo + 1]

    def renovarPilha(self):
        self.topo = -1

P = Pilha(100)

def flatten(lista):
    for i in lista:
        if isinstance(i, list):
            flatten(i)
        else:
            P.push(i)
    return P.listaPilha()

 # Teste padrões exercício
P.renovarPilha()
assert flatten([1, [2, [3, 4], 5], 6])  == [1, 2, 3, 4, 5, 6]
P.renovarPilha()
print(flatten([1, [2, [3, 4], 5], 6]))

P.renovarPilha()
assert flatten([[1, 2], [3, [4, [5]]]]) == [1, 2, 3, 4, 5]
P.renovarPilha()
print(flatten([[1, 2], [3, [4, [5]]]]))

# Testes edge cases

P.renovarPilha()
# Lista vazia []
assert flatten([]) == []
P.renovarPilha()
print(flatten([]))

P.renovarPilha()
# Lista sem nenhum aninhamento [1, 2, 3]
assert flatten([1, 2, 3]) == [1, 2, 3]
P.renovarPilha()
print(flatten([1, 2, 3]))

P.renovarPilha()
# Lista com sublistas vazias [[], [[], []], 1]
assert flatten([[], [[], []], 1]) == [1]
P.renovarPilha()
print(flatten([[], [[], []], 1]))

P.renovarPilha()
# Aninhamento muito profundo [[[[[1]]]]]
assert flatten([[[[[1]]]]]) == [1]
P.renovarPilha()
print(flatten([[[[[1]]]]]))

P.renovarPilha()
# Lista com apenas 1 elemento [42]
assert flatten([42]) == [42]
P.renovarPilha()
print(flatten([42]))

# Responda: Qual é a complexidade de tempo e de espaço da sua solução? Use a notação O.
# Apesar de alguns casos possuirem aninhamento profundo, o script só percorre apenas 1 vez cada item, por tanto, podemos dizer que a complexidade é O(n).