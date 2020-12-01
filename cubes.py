import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 8, 27, 64, 125]
#
# plt.scatter(x_values, y_values, s=200)

x_values = list(range(1, 5000))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=12)

plt.title("Cubes", fontsize=20)
plt.xlabel("Cube of Values", fontsize=12)
plt.ylabel("Values", fontsize=12)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 5000, 0, 125000000000])
#
# plt.savefig('squares_plot.png', bbox_inches='tight')

plt.show()
