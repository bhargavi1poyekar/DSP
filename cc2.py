import matplotlib.pyplot as plt
xn = list(map(int, input("Enter the values of x[n]:\n").split()))
hn = list(map(int, input("Enter the values of h[n]:\n").split()))

xlen=len(xn)
hlen=len(hn)

nmax=max(xlen,hlen)
rg=xlen+hlen-1

yn = [0]*rg
for i in range(len(xn)):
    for j in range(len(hn)):
        yn[i+j] += xn[i]*hn[j]

print("\nTabular form\n")

print("  "+str(xn))
print("-"*15)
for j in range(len(hn)):
    print(str(hn[j]) + "|", end="  ")
    for i in range(len(xn)):

        print(xn[i]*hn[j], end="  ")
    print("\n")

print(yn)

k=0
for i in range(nmax,len(yn)):
    yn[k]+=yn[i]
    k+=1
	
print("y[n] is:")
print(yn[:nmax])

xrange = list(range(0, xlen))
hrange = list(range(0, hlen))
yrange = list(range(0, nmax))
plt.subplot(311)
plt.stem(xrange, xn, use_line_collection=True)
plt.title("x[n] Input Signal")

plt.subplot(312)
plt.stem(hrange, hn, use_line_collection=True)
plt.title("\n h[n] Impulse Signal")

plt.subplot(313)
plt.stem(yrange, yn[:nmax], use_line_collection=True)
plt.title("\n y[n] Convoluted Signal")
plt.show()
