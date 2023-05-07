def f(x):
    return x**3 - x**2 - 1

def bisseccao(xa, xb, e):
    passo = 1
    print("\t\t***Implementação do Método da Bissecção***")
    condicao = True
    while condicao and passo < 100:
        xc = (xa + xb)/2
        print(f"Iteração: {passo}|xa = {xa:.6f}|xb = {xb:.6f}|xc = {xc:.6f}|f(x) = {f(xc):.6f}")
        if f(xa) * f(xc) < 0:
            xb = xc
        else:
            xa = xc

        passo += 1
        condicao = abs(f(xc)) > e
    if passo == 100:
        print("O método não convergiu para 100 iterações!")
    else:
        print(f"O método convergiu para {passo} iterações. A raiz aproximada é {xc:.6f}!")


bisseccao(1,2, 0.0001)
