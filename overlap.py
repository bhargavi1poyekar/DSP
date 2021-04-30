import matplotlib.pyplot as plt
xn = list(map(int, input("Enter the values of x[n]:\n").split()))
hn = list(map(int, input("Enter the values of h[n]:\n").split()))
Ls = len(xn)
M = len(hn)
L = int(input("Enter the value of L: "))
N = L+M-1
hn.extend([0] * (N-M))
print("\nxn= " + str(xn))
print("hn= " + str(hn))
print("Ls=", end=" ")
print(Ls)
print("M=", end=" ")
print(M)
print("L=", end=" ")
print(L)
print("N=", end=" ")
print(N)
print("\n")

n_blks = Ls//L
if(Ls % L != 0):
    n_blks += 1

x = [[] for j in range(n_blks)]
for i in range(M-1):
    x[0].append(0)

idx = 0
for i in range(n_blks-1):
    for j in range(L):
        if(idx < 10):
            x[i].append(xn[idx])
            idx += 1
        else:
            x[i].append(0)
    for k in range(M-1, 0, -1):
        x[i+1].append(xn[idx-k])

for i in range(L):
    if(idx < 10):
        x[n_blks-1].append(xn[idx])
        idx += 1
    else:
        x[n_blks-1].append(0)


for i in range(n_blks):
    print("X", end="")
    print(i, end="")
    print("(n)=", end=" ")
    print(x[i])

# Convolution

def convolution(l1, l2):
    xlen = len(l1)
    hlen = len(l2)

    nmax = max(xlen, hlen)
    rg = xlen+hlen-1

    yn = [0]*rg
    for i in range(len(l1)):
        for j in range(len(l2)):
            yn[i+j] += l1[i]*l2[j]

    k = 0
    for i in range(nmax, len(yn)):
        yn[k] += yn[i]
        k += 1

    return yn[:nmax]


y = [[] for j in range(n_blks)]

for i in range(n_blks):
    y[i] = convolution(x[i], hn)

print("\n")

for i in range(n_blks):
    print("Y", end="")
    print(i, end="")
    print("(n)=", end=" ")
    print(y[i])

yn = []

for i in range(n_blks):
    for j in range(M-1, N, 1):
        yn.append(y[i][j])

print("\nY(n)= ", end=" ")
print(yn)
