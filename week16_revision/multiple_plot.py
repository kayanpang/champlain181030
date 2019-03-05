import matplotlib.pyplot as plt

squares = [10, 20, 30, 40, 50]
input_values = [10, 20, 30, 40, 50]
plt.plot(squares)


# line width, title, XY labels, Tick labels
plt.plot(input_values, squares, linewidth=5)
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis="both", labelsize=14)
plt.show()