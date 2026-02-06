import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def cost_analysis(x):
    production_cost_per_game = 5000
    cost_per_x_copy = 12 * x
    return cost_per_x_copy + production_cost_per_game

def graph_cost_analysis():
    import matplotlib.pyplot as plt
    x_values = range(1, 1001)
    y_values = [cost_analysis(x) for x in x_values]
    plt.plot(x_values, y_values)
    plt.xlabel('Number of Copies (x)')
    plt.ylabel('Total Cost')
    plt.title('Cost Analysis of Game Production')
    plt.grid() 
    plt.show() 

graph_cost_analysis()