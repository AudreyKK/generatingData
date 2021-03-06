import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get high temps from this file.

filename = 'sitka_weather_2018_full.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:

        # This is the try-except-esle sequence for the sitka data sheet
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            high = int(row[8])
            low = int(row[9])
        # The value errors don't seem to get thrown at all when data is missing
        except ValueError:
            print(current_date, 'missing data')

        except IndexError:
            # Index errors get thrown when I use differently formatted data sheets
            try:
                current_date = datetime.strptime(row[2], "%Y-%m-%d")
                high = int(row[7])
                low = int(row[6])
            except ValueError:
                print(current_date, 'missing data')

            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

            # The above segment is a messy solution to handle differently
            # formatted datasheets. I'm just learning about using the plots
            # themselves and not parsing and reformatting .csv files.
            # I COULD have just made another file, but I did not.

filename2 = 'death_valley_2018_full.csv'
with open(filename2) as f2:
    reader = csv.reader(f2)
    header_row = next(reader)

    dates_dv, highs_dv, lows_dv = [], [], []
    for row in reader:

        # This is the try-except-esle sequence for the sitka data sheet
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            high = int(row[8])
            low = int(row[9])
        # The value errors don't seem to get thrown at all when data is missing
        except ValueError:
            print(current_date, 'missing data')

        except IndexError:
            # Index errors get thrown when I use differently formatted data sheets
            try:
                current_date = datetime.strptime(row[2], "%Y-%m-%d")
                high = int(row[6])
                low = int(row[7])
            except ValueError:
                print(current_date, 'missing data')

            else:
                dates_dv.append(current_date)
                highs_dv.append(high)
                lows_dv.append(low)

        else:
            dates_dv.append(current_date)
            highs_dv.append(high)
            lows_dv.append(low)


# Plot data.

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.plot(dates_dv, highs_dv, c='orange', alpha=0.5)
plt.plot(dates_dv, lows_dv, c='green', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.fill_between(dates_dv, highs_dv, lows_dv, facecolor='green', alpha=0.1)

# Format plot.
plt.title("Daily high and low temperatures - 2018\nDeath Valley, CA and Sitka, AK", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
