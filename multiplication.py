from die import Die

import pygal

die_1 = Die()
die_2 = Die()

rolls = 1000
results = [(die_1.roll() * die_2.roll()) for x in list(range(1, rolls+1))]

frequencies = [results.count(i) for i in list(range(1, 36+1))]

hist = pygal.Bar()

hist.title = "Results of D6 multiplied by D6"
hist.x_labels = list(range(1, 36+1))
hist.x_title = "Results"
hist.y_title = "Frequencies"

hist.add("D6 * D6", frequencies)
hist.render_to_file("die_visual.svg")
