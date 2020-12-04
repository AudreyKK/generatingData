from die import Die

import pygal

# Create a D6 and a D10

die_1 = Die(8)
die_2 = Die(8)

die_1_label = "D8"
die_2_label = "D8"

rolls = 1000
results = [(die_1.roll() + die_2.roll()) for x in list(range(1, rolls+1))]

# Create an empty array to store frequencies.
frequencies = []
for i in range(2, (die_1.num_sides + die_2.num_sides) + 1):
    frequency = results.count(i)
    frequencies.append(frequency)

max_results = die_1.num_sides + die_2.num_sides
frequencies = [results.count(i) for i in list(range(2, max_results + 1))]

# Visualize results
hist = pygal.Bar()

pt1 = "Results of rolling a " + die_1_label + " and a "
pt2 = die_2_label + " " + str(rolls) + " times"
title = pt1 + pt2
hist.title = title
hist.x_labels = range(2, (die_1.num_sides + die_2.num_sides)+1)
hist.x_title = "Results"
hist.y_title = "Frequency of Results"

hist.add(die_1_label + " + " + die_2_label, frequencies)
hist.render_to_file("die_visual.svg")
