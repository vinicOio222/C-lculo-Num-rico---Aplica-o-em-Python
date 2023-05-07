def f(x):
    return x**2 - 7

def dx_f(x):
    return 2*x

def g(x):
    return x - (f(x)/dx_f(x))

def newton_raphson(a_i):
    x = g(a_i)
    print(f"x = {a_i:.6f}|f(x) = {f(a_i):.6f}|g(x) = {g(a_i):.6f}")
    i = 0
    while abs(f(x)) > 0.00001 and i < 100:
        i+=1
        print(f"x = {x:.6f}|f(x) = {f(x):.6f}|g(x) = {g(x):.6f}")
        x = g(x)

    if i == 100:
        print(f"O método não convergiu para 100 iterações!")
    else:
        print(f"x = {x:.6f}|f(x) = {f(x):.6f}|g(x) = {g(x):.6f}")
        print(f"A raíz aproximada é {x:.6f}! O método convergiu após {i+2} iterações!")

newton_raphson(2)

