
import numpy as np
import math
import matplotlib.pyplot as plt

N_sequence = int(input("Enter the value of N: "))

while((N_sequence & N_sequence-1) != 0 or N_sequence == 0):

    N_sequence = int(
        input("\nEntered value of N must be power of 2 \nEnter the value of N: "))

input_sequence = []

for i in range(0, N_sequence):
    input_sequence.append(complex(input(f"\nEnter {i+1} th element: ")))


def dft(xn):
    x = np.asarray(xn)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    Wn = np.exp(-2j*np.pi*k*n/N)
    return np.dot(Wn, x)


dft(input_sequence)


def fft(xn):
    x = np.asarray(xn)
    N = x.shape[0]
    if N == 2:
        return dft(x)
    else:
        gk = fft(x[::2])
        hk = fft(x[1::2])
        wn = np.exp(-2j*np.pi*np.arange(N)/N)
        return np.concatenate([gk + wn[:int(N/2)]*hk, gk + wn[int(N/2):]*hk])


Xk = fft(input_sequence)

print("\nOutput Sequence: \n")
for i in range(0, N_sequence):
    print(f"X[{i}] = ", end='')
    print("{0:.2f}".format(Xk[i]))

# Commented out IPython magic to ensure Python compatibility.
a = np.random.rand(256)
print("Time taken for DFT:", end=' ')
# %timeit dft(a)
print("Time taken for FFT:", end=' ')
# %timeit fft(a)
