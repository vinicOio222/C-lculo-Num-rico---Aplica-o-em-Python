import numpy as np
import matplotlib.pyplot as plt

x = np.array([-1,0,1,2,3,4,5,6])
y = np.array([10,9,7,5,4,3,0,-1])

Sum_1 = 0
for i in range(len(x)):
    Sum_1 += 1

Sum_xi = x.sum()

Sum_xi2 = 0
for i in range(len(x)):
    Sum_xi2 += x[i]**2

Sum_yi = y.sum()

Sum_xiyi = 0
for i in range(len(x)):
    Sum_xiyi += x[i]*y[i]

print(f"∑1 = {Sum_1}")
print(f"∑xi = {Sum_xi}")
print(f"∑xi^2= {Sum_xi2}")
print(f"∑yi = {Sum_yi}")
print(f"∑xiyi = {Sum_xiyi}")
print("\n")

print("Sistema linear:")
print(np.array([[Sum_1, Sum_xi],[Sum_xi, Sum_xi2]]))
print("   *")
print(np.array([["a"],["b"]]))
print("   =")
print(np.array([[Sum_yi],[Sum_xiyi]]))

n = len(x)
x_mean = np.mean(x)
y_mean = np.mean(y)

numerator = np.sum((x - x_mean)*(y-y_mean))
denominator = np.sum((x - x_mean)**2)

m = numerator/denominator
b = y_mean - m*x_mean

print(f"Função: g(x) = {b:.4f} + {m:.4f}x")
plt.scatter(x,y)
plt.plot(x, m*x + b, color = 'red')
plt.show
