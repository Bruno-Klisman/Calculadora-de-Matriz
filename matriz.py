import numpy as np

def criar_matriz(nome_matriz):
    linhas = int(input(f"\nDigite o número de linhas da matriz {nome_matriz}: "))
    colunas = int(input(f"\nDigite o número de colunas da matriz {nome_matriz}: "))
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            elemento = float(input(f"\nDigite o elemento na posição ({i+1}, {j+1}) da matriz {nome_matriz}: "))
            linha.append(elemento)
        matriz.append(linha)
    return np.array(matriz)

def somar_matrizes(matriz1, matriz2):
    return matriz1 + matriz2

def subtrair_matrizes(matriz1, matriz2):
    return matriz1 - matriz2

def multiplicar_matrizes(matriz1, matriz2):
    return np.dot(matriz1, matriz2)

def calcular_determinante(matriz):
    return np.linalg.det(matriz)

while True:
    opcao = int(input("\n\n|-- Escolha uma opção: --|\n1. Somar duas matrizes\n2. subitração de duas matrizes\n3. Multiplicar duas matrizes\n4. Divisão de duas matrizes\n5. Calcular o determinante de uma matriz\n6. Sair\n"))

    if opcao == 1:
        matriz_A = criar_matriz("A")
        matriz_B = criar_matriz("B")
        resultado = somar_matrizes(matriz_A, matriz_B)
        print("\nA soma das matrizes é:\n", resultado)
    elif opcao == 2:
        matriz_A = criar_matriz("A")
        matriz_B = criar_matriz("B")
        resultado = subtrair_matrizes(matriz_A, matriz_B)
        print("\nA subtração das matrizes é:", resultado)
    elif opcao == 3:
        matriz_A = criar_matriz("A")
        matriz_B = criar_matriz("B")
        if matriz_A.shape[1] == matriz_B.shape[0]:
            resultado = multiplicar_matrizes(matriz_A, matriz_B)
            print("\nO produto das matrizes é:", resultado)
        else:
            print("\nO número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
    elif opcao == 4:
        matriz_A = criar_matriz("A")
        matriz_B = criar_matriz("B")
        determinante_B = calcular_determinante(matriz_B)

        if matriz_A.shape[1] == matriz_B.shape[0]:
            if determinante_B != 0:
                try:
                    matriz_inversa_B = np.linalg.inv(matriz_B)
                    resultado = np.dot(matriz_A, matriz_inversa_B)
                    print("\nA divisão das matrizes é:\n", resultado)
                except np.linalg.LinAlgError:
                    print("\nA matriz B não é invertível.")
            else:
                print("\nO determinante de B é zero, portanto não é invertível.")
        else:
            print("\nO número de colunas de A deve ser igual ao número de linhas de B para a multiplicação.")
    elif opcao == 5:
        matriz = criar_matriz("M")
        determinante = calcular_determinante(matriz)
        print("\nO determinante da matriz é:", determinante)

    elif opcao ==6:
        break

    else:
        print("\nOpção inválida. Tente novamente.")