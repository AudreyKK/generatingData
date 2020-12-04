from die import Die

import pygal

die_1 = Die()
die_2 = Die()
die_3 = Die()

# need to add at least two dice
def add_dice(first_die, sec_die, *dice):
    res = first_die.roll() + sec_die.roll()
    for d in dice:
        res += d.roll()
    return res

rolls = 1000
results = [add_dice(die_1, die_2, die_3) for x in list(range(1, rolls+1))]

max_results = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(i) for i in list(range(3, max_results+1))]

hist = pygal.Bar()

hist.title = "Results of 3xD6 rolled 1000 times"
hist.x_labels = list(range(3, max_results+1))
hist.x_title = "Results"
hist.y_title = "Frequencies"

hist.add("D6 + D6 + D6", frequencies)
hist.render_to_file("die_visual.svg")
