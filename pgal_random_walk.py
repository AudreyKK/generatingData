import pygal

from random_walk import RandomWalk

# Make random walk, and plot points
rw = RandomWalk(50000)
rw.fill_walk()

merged_values = [(rw.x_values[i], rw.y_values[i]) for i in list(range(0, len(rw.x_values)))]


scatter = pygal.XY(stroke=False)
scatter.add("step", merged_values)

scatter.render_to_file('random_walk.svg')
