import matplotlib.pyplot as plt
xn = list(map(float, input("Enter the values of x[n]:\n").split()))
xo = int(input("Enter the origin index: "))
hn = list(map(float, input("Enter the values of h[n]:\n").split()))
ho = int(input("Enter the origin index: "))

lx = -xo
lh = -ho
ly = lx+lh

hx = len(xn)-1-xo
hh = len(hn)-1-ho
hy = hx+hh

rg = hy-ly+1
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

print("y[n] is:")
print(yn)
print("The range of y is from "+str(ly)+" to "+str(hy))

xrange = list(range(lx, hx+1))
hrange = list(range(lh, hh+1))
yrange = list(range(ly, hy+1))
plt.subplot(311)
plt.stem(xrange, xn, use_line_collection=True)
plt.title("x[n] Input Signal")

plt.subplot(312)
plt.stem(hrange, hn, use_line_collection=True)
plt.title("\n h[n] Impulse Signal")

plt.subplot(313)
plt.stem(yrange, yn, use_line_collection=True)
plt.title("\n y[n] Convoluted Signal")
plt.show()
