import math

def gaussPivotamento(A, b):
    for i in range(len(A)):
        pivo = math.fabs(A[i][i])
        linhaPivo = i
        for j in range(i+1, len(A)):
            if math.fabs(A[j][i]) > pivo:
                pivo = math.fabs(A[j][i])
                linhaPivo = j
        if linhaPivo != i:
            linhaAuxiliar = A[i]
            A[i] = A[linhaPivo]
            A[linhaPivo] = linhaAuxiliar
            bAuxiliar = b[i]
            b[i] = b[linhaPivo]
            b[linhaPivo] = bAuxiliar
        for m in range(i+1, len(A)):
            multiplicador = A[m][i]/A[i][i]
            for n in range(i, len(A)):
                A[m][n] -= multiplicador*A[i][n]
            b[m] -= multiplicador*b[i]
    print("Matriz A pivotada:\n")
    for k in range(len(A)):
        print(A[k])
    print()
    print("Vetor b:\n")
    print(b)
    print()
    calculaSoma(A,b)

def calculaSoma(A, b):
    vetorSolucao = []
    for i in range(len(A)):
        vetorSolucao.append(0)
    linha = len(A) - 1
    while linha >= 0:
        x = b[linha]
        coluna = len(A) - 1
        while coluna > linha:
            x -= A[linha][coluna]*vetorSolucao[coluna]
            coluna -= 1
        x /= A[linha][linha]
        linha -= 1
        vetorSolucao[coluna] = x
    print("Resultados:\n")
    for j in range(len(vetorSolucao)):
        print(f"x{j+1} = {vetorSolucao[j]:.2f}")

gaussPivotamento([[3.0,2.0,4.0],[2.0,2.0,3.0],[3.0,3.0,5.0]], [80.0, 60.0,95.0])
