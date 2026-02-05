import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def find_y(x):
    return 0*x-2

points = [3, 5, 8, -1, -11]
y_values = [find_y(x) for x in points]


plt.plot(points, y_values, marker='o')
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = -2")
plt.grid(True)
plt.show()