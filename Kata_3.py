# Problema 3: O Bug do Inventário
# Um desenvolvedor de jogos estava criando um sistema de inventário 2D (uma grade de 3x3 espaços) para um novo RPG. Ele inicializou todos os espaços com a string "Vazio".

# Quando o jogador pega uma "Espada" e a coloca no primeiro espaço ([0][0]), um bug bizarro acontece: a espada é clonada e aparece em três lugares ao mesmo tempo!

# O Código com Bug:
# def criar_inventario():
#     # Cria uma linha com 3 espaços vazios
#     linha = ["Vazio", "Vazio", "Vazio"]
#     # Cria a grade multiplicando a linha por 3
#     inventario = [linha] * 3
#     return inventario

# inv = criar_inventario()

# # Coloca a espada no primeiro espaço (linha 0, coluna 0)
# inv[0][0] = "Espada"

# for linha in inv:
#     print(linha)

# # Saída no terminal:
# # ['Espada', 'Vazio', 'Vazio']
# # ['Espada', 'Vazio', 'Vazio']
# # ['Espada', 'Vazio', 'Vazio']
# Sua Missão
# Explicar o Bug: Usando o modelo mental de memória (Stack, Heap, referências, ponteiros, aliasing) ensinado na Aula 04, explique de forma clara por que esse bug acontece. Não basta dizer "multiplicar lista é ruim", explique como os dados estão organizados na memória.
# Corrigir o Código: Escreva uma versão corrigida da função criar_inventario() que não sofra desse bug, garantindo que inv[0][0] = "Espada" modifique apenas o primeiro slot.