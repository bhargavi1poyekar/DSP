import numpy as np
import math

xn = list(map(float, input("Enter the discrete values for signal:\n").split()))

N = len(xn)

add = [0]*N
comp = 0-1j

for k in range(N):
    for n in range(N):
        add[k] = add[k]+xn[n]*((np.exp((math.pi*2/N)*comp))**(n*k))

for xk in range(N):
    add[xk] = np.round(add[xk].real, 2)+np.round(add[xk].imag, 2)*1j
print("\nx(k) is: \n")
print(add)
