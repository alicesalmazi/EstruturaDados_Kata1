def fatorial(n):
    if n <= 1:
        return 1

    return n * fatorial(n - 1)
    # Custo de O(n)

# assert fatorial(0) == 1 # Fatorial de 0 (esperado 1)
# print(fatorial(0)) # Fatorial de 0 (esperado 1)
# assert fatorial(1) == 1 # Fatorial de 1 (esperado 1)
# print(fatorial(1)) # Fatorial de 1 (esperado 1)
# assert fatorial(5) == 120 # Fatorial de 5 (esperado 120)
# print(fatorial(5)) # Fatorial de 5 (esperado 120)

def fibonacci(n):
    if n <= 1:
        return 1
    
    return fibonacci(n -1) + fibonacci(n - 2)
    # Custo de O(2ⁿ)

# Criando o nó
class Node:
    def __init__(self, data):
        self.data = data # Cria o espaço do dado
        self.next = None # Cria o espaço do ponteiro do próx dado

# Lista encadeada 
class LinkedList:
    def __init__(self):
        self.head = None # Define a cabeça (está vazia)

    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

# Em python a função id() retorna a memória do objeto (a is b)

# Pilha encadeada
class pilhaEncadeada:
    def __init__(self):
        self.head = None

    def push(self, dado):
        novo = Node(dado)

        novo.prox = self.head

        self.head = novo

    def pop(self):
        if self.head is None:
            raise Exception("Underflow")
        
        valor = self.head.dado

        self.head = self.head.prox

        return valor

# Conferência de abertura e fechamento

# Pilha em arranjo
class PilhaArray:
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
            raise Exception("Underflow")

        valor = self.array[self.topo]
        self.topo -= 1
        return valor

    def peek(self):
        return self.array[self.topo]

    def is_empty(self):
        return self.topo == -1


def validar_parenteses():
    P = PilhaArray()
    aberturas = ['(','[', '{']
    fechamentos = [')', ']', '}']
    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in expressao:
        abertura = char in aberturas
        fechamento = char in fechamentos

        if abertura:
            P.push(char)
        
        if fechamento:
            anterior = P.pop()
            anterior_esperado = pares[char]

            if anterior != anterior_esperado:
                return false
    
    return P.is_empty()

# ==========================================
# CASOS DE TESTE
# ==========================================

def test_pilha_push_e_pop():
    p = Pilha()
    p.push(10)
    p.push(20)
    p.push(30)
    assert p.pop() == 30
    assert p.pop() == 20
    assert p.pop() == 10

def test_pilha_peek_nao_remove():
    p = Pilha()
    p.push(42)
    assert p.peek() == 42
    assert p.peek() == 42  # continua la
    assert p.pop() == 42

def test_pilha_is_empty():
    p = Pilha()
    assert p.is_empty() is True
    p.push(1)
    assert p.is_empty() is False
    p.pop()
    assert p.is_empty() is True

def test_pilha_pop_vazia_levanta_erro():
    import pytest
    p = Pilha()
    with pytest.raises(IndexError):
        p.pop()

def test_pilha_peek_vazia_levanta_erro():
    import pytest
    p = Pilha()
    with pytest.raises(IndexError):
        p.peek()

def test_pilha_ordem_lifo():
    p = Pilha()
    for i in range(5):
        p.push(i)
    for i in range(4, -1, -1):
        assert p.pop() == i

def test_parenteses_simples():
    assert validar_parenteses("()") is True

def test_todos_os_tipos():
    assert validar_parenteses("()[]{}") is True

def test_tipo_errado():
    assert validar_parenteses("(]") is False

def test_intercalado_errado():
    assert validar_parenteses("([)]") is False

def test_comeca_fechando():
    assert validar_parenteses("]") is False

def test_nunca_fecha():
    assert validar_parenteses("[") is False

# --- Testes extras de borda ---

def test_string_vazia():
    assert validar_parenteses("") is True

def test_aninhado_profundo():
    assert validar_parenteses("{[({[(())]})]}") is True

def test_texto_sem_parenteses():
    assert validar_parenteses("abc + 123") is True

def test_mistura_com_texto():
    assert validar_parenteses("func(a[0], {b: 1})") is True

def test_fecha_mais_que_abre():
    assert validar_parenteses("())") is False

def test_abre_mais_que_fecha():
    assert validar_parenteses("(()") is False