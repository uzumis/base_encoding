import matplotlib.pyplot as plt


str = input("Insira sua sequência de bits ")
n = len(str)
x = list()
y = list()

#Manchester Diferencial
for i in range(n):
    y.append(int(str[i]))

progress = list()

for i in range(n - 1):
    if i == 0:
        if y[i] == 1:
                progress.append(1)
                progress.append(-1)
        elif y[i] == 0:
                progress.append(-1)
                progress.append(1)
    if y[i + 1] == 0:
        if progress[-1] == -1:
                progress.append(1)
                progress.append(-1)
        elif progress[-1] == 1:
                progress.append(-1)
                progress.append(1)
    if y[i + 1] == 1:
        if progress[-1] == -1:
                progress.append(-1)
                progress.append(1)
        elif progress[-1] == 1:
                progress.append(1)
                progress.append(-1)

encoding = []

for i in progress:
    encoding.extend([i, i])

progress = encoding

for i in range(2 * n):
        x.append(i)

x = x * 2
x.sort()
x.remove(x[0])
x.append(2 * n)

zero = list()

for i in range(0, 4 * n):
    zero.append(int(0))
#Exibe o gráfico
plt.plot(x, progress, marker="None", color="black",drawstyle="steps-pre")
plt.plot(x, zero,marker="None", color="black",drawstyle="steps-pre")
plt.plot([0, 0, 0], [0, 1.5, -1.5])
plt.grid()
plt.title("Manchester Diferencial")
plt.show()