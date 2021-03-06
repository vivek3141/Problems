import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

x1 = [4.58, 9.48, 14.386]
y1 = [0.882, 1.764, 2.646]
slope = (y1[0] - y1[2]) / (x1[0] - x1[2])


def func(x, a, b):
    return (x * a) + b


def plot(x_data, y_data, color):
    i = [1, 1]
    t = curve_fit(func, x_data, y_data, i)
    print(t[0])
    xd = np.linspace(min(x_data), max(x_data), 100)
    line = [func(x, *t[0]) for x in xd]
    rounded = list(map(lambda x: round(x, 2), t[0]))
    l = "{}x+ {}".format(*rounded)
    plt.plot(xd, line, color=color, label=l)


plt.title("$F_k$ vs $F_n$ for Wood + Wood")
plt.xlabel(r"$F_k$ (N)")
plt.ylabel("$F_n$ (N)")
plt.scatter(x1, y1, color="g")
plot(x1, y1, color="g")
plt.legend(loc="upper left")
plt.savefig("./Graphs/force_2.png")
plt.show()
