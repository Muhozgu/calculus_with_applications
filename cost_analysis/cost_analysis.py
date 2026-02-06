def cost_analysis(x):
    production_cost_per_game = 5000
    cost_per_x_copy = 12 * x
    return cost_per_x_copy + production_cost_per_game

print(cost_analysis(1000))