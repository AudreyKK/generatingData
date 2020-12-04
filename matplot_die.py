import matplotlib.pyplot as plt
from die import Die

die_1 = Die()
die_2 = Die()

rolls = 5000
results = [(die_1.roll() + die_2.roll()) for x in list(range(1, rolls+1))]

max_results = die_1.num_sides + die_2.num_sides
frequencies = [results.count(i) for i in list(range(2, max_results+1))]


plt.hist(results, list(range(2, max_results+1)), outline='black')
plt.title("2xD6 rolled 5000 times")
plt.xlabel("Results")
plt.ylabel("Frequencies")
plt.tick_params(axis='both', labelsize=10)

plt.show()
