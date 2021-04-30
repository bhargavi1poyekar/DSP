import numpy as np
import math

xk = list(map(complex, (input("Enter the discrete values for signal:\n").split())))

N = len(xk)

add = [0+0j]*N

for k in range(N):
    for n in range(N):
        add[k] = add[k]+xk[n] * \
            ((np.cos(math.pi*2/N)+(np.sin(math.pi*2/N)*1j))**(n*k))
    add[k] /= N

for xk in range(N):
    add[xk] = np.round(add[xk].real, 2)

print("\nx(n) is: \n")
print(add)
