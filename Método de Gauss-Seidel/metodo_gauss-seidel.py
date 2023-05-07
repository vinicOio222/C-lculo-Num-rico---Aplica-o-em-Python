from math import *
import copy

A = [[4,-2,-1,0],[-2, 9,0,-5],[-1,0,6,-3],[0,-5,-3,10]]
b = [10,-5,0,0]

def convergencia():
    for i in range(b.__len__()):
        aii = abs(A[i][i])
        aji = 0
        for j in range(b.__len__()):
            if(j!=i):
                aji += abs(A[i][j])
        print(aii, aji)
    return True

def round_(x = list, casas = int):
    xteste = []
    for i in range(x.__len__()):
        xteste.append(round(x[i], casas))
        return xteste

def gauss_seidel():
    cont = 0
    e = 1
    x = [0, 0, 0, 0]
    xAnt = copy.deepcopy(x)
    while e>=0.001 and cont < 100:
        xAnt = copy.deepcopy(x)
        for i in range(x.__len__()):
            xi = 0
            for j in range(x.__len__()):
                if(i != j):
                    xi+= (-1)*A[i][j]*x[j]/A[i][i]
            xi+=b[i]/A[i][i]
            x[i] = xi
        cont += 1
        e = 0
        for i in range(x.__len__()):
            e += (xAnt[i] - x[i])*(xAnt[i] - x[i])
        e = sqrt(e)
        print(f"x1^k = {xAnt[0]:.3f}|x2^k = {xAnt[1]:.3f}|x3^k = {xAnt[2]:.3f}|x4^k = {xAnt[3]:.3f}|x1^k+1 = {x[0]:.3f}"
              +f"|x2^k+1 = {x[1]:.3f}|x3^k+1 = {x[2]:.3f}|x4^k+1 = {x[3]:.3f}| Δ = {e:.3f}")

    if cont == 100:
        print("O método não convergiu após 100 iterações!")
    else:
        print(f"O método convergiu após {cont} iterações!")

gauss_seidel()


