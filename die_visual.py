import pygal
from die import Die

# Create a D6
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    sum = die_1.roll() + die_2.roll()
    results.append(sum)

# Analyze the results.
frequencies = []
for value in range(2, (die_1.num_sides + die_2.num_sides)+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visulaize the results.
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
