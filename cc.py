import matplotlib.pyplot as plt

xn = list(map(float, input("Enter the values of x[n]:\n").split()))
hn = list(map(float, input("Enter the values of h[n]:\n").split()))

# making length of list equal by padding zero
if len(xn) > len(hn):
    diff = len(xn)-len(hn)
    for i in range(diff):
        hn.append(0)
elif len(xn) < len(hn):
    diff = len(hn)-len(xn)
    for i in range(diff):
        xn.append(0)

length = len(xn)

shift = [[0 for i in range(length)] for j in range(length)]
circular_shift = [[0 for i in range(length)] for j in range(length)]

# creating circular shift matrix
for i in range(length):
    shift[i] = xn[length-i:length] + xn[0:length-i]

for i in range(length):
    # iterate through columns
    for j in range(length):
        circular_shift[j][i] = shift[i][j]

print("\nCircular Shift Matrix:\n")
for i in range(length):
    print(circular_shift[i])

# declaring yn
yn = [0 for i in range(length)]

for i in range(length):
    for j in range(length):
        yn[i] += circular_shift[i][j] * hn[j]

print("\ny(n)=", end=" ")
print(yn)

range = list(range(0, length))

plt.subplot(311)
plt.stem(range, xn, use_line_collection=True)
plt.title("x[n] Input Signal")

plt.subplot(312)
plt.stem(range, hn, use_line_collection=True)
plt.title("\n h[n] Impulse Signal")

plt.subplot(313)
plt.stem(range, yn, use_line_collection=True)
plt.title("\n y[n] Convoluted Signal")
plt.show()
