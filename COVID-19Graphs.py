import urllib.request
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
request_url = urllib.request.urlopen(url)
lines = request_url.readlines()

names = [str(line).split(',')[5] for line in lines]

sc_index = names.index("Santa Clara")
sc_data = str(lines[sc_index]).split(',')[13:-1]
sc_new_cases = [int(sc_data[i + 1]) - int(sc_data[i]) for i in range(len(sc_data) - 1)]

sd_index = names.index("San Diego")
sd_data = str(lines[sd_index]).split(',')[13:-1]
sd_new_cases = [int(sd_data[i + 1]) - int(sd_data[i]) for i in range(len(sd_data) - 1)]

alameda_index = names.index("Alameda")
alameda_data = str(lines[alameda_index]).split(',')[13:-1]
alameda_new_cases = [int(alameda_data[i + 1]) - int(alameda_data[i]) for i in range(len(alameda_data) - 1)]

ny_index = names.index("New York")
ny_data = str(lines[ny_index]).split(",")[13:-1]
ny_new_cases = [int(ny_data[i + 1]) - int(ny_data[i]) for i in range(len(ny_data) - 1)]

sf_index = names.index("San Francisco")
sf_data = str(lines[sf_index]).split(',')[13:-1]
sf_new_cases = [int(sf_data[i + 1]) - int(sf_data[i]) for i in range(len(sf_data) - 1)]

la_index = names.index("Los Angeles")
la_data = str(lines[la_index]).split(',')[13:-1]
la_new_cases = [int(la_data[i + 1]) - int(la_data[i]) for i in range(len(la_data) - 1)]

# -----------------------------------------------------

y = [int(val) for val in sc_data]
y2 = [int(val) for val in sd_data]
y3 = [int(val) for val in alameda_data]
y4 = [int(val) for val in sf_data]
y5 = [int(val) for val in la_data]
y6 = [int(val) for val in ny_data]

x = [i for i in range(len(sc_new_cases))]
x2 = [i for i in range(len(sd_new_cases))]
x3 = [i for i in range(len(alameda_new_cases))]
x4 = [i for i in range(len(sf_new_cases))]
x5 = [i for i in range(len(la_new_cases))]
x6 = [i for i in range(len(ny_new_cases))]

plt.subplot(6, 2, 1);
plt.title("Daily New Coronavirus Cases in Santa Clara")
plt.xlabel("time (days)")
plt.ylabel("# people")
plt.bar(x, sc_new_cases, color=(0, 0, 0, 1));

plt.subplot(6, 2, 2);
plt.title("Total Coronavirus Cases in Santa Clara")
plt.xlabel("time (days)")
plt.ylabel("# people")
plt.plot(y, 'k-.', label="Santa Clara")

plt.subplot(6, 2, 3);
plt.title("Daily New Coronavirus Cases in San Diego")
plt.xlabel("time (days)")
plt.ylabel("# people")
plt.bar(x2, sd_new_cases, color=(0.2, 0.2, 1, 1));

plt.subplot(6, 2, 4);
plt.title("Total Coronavirus Cases in San Diego")
plt.xlabel("time (days)")
plt.ylabel("# people")
plt.plot(y2, 'b-.', label="San Diego")

plt.subplot(6, 2, 5);
plt.title("Daily New Coronavirus Cases in Alameda")
plt.xlabel("time (days)")
plt.ylabel("# people")
plt.bar(x3, alameda_new_cases, color=(1, 0.2, 0.2, 1));

plt.subplot(6, 2, 6);
plt.title("Total Coronavirus Cases in Alameda")
plt.xlabel("time (days)")
plt.ylabel("# people")
plt.plot(y3, 'r-.', label="Alameda")

plt.subplot(6, 2, 7);
plt.title("Daily New Coronavirus Cases in San Francisco")
plt.xlabel("time (days)")
plt.ylabel("# people")
plt.bar(x4, sf_new_cases, color=(0.8, 0.85, 0.4, 1));

plt.subplot(6, 2, 8);
plt.title("Total Coronavirus Cases in San Francisco")
plt.xlabel("time (days)")
plt.ylabel("# people")
plt.plot(y4, 'y-.', label="San Francisco")

plt.subplot(6, 2, 9);
plt.title("Daily New Coronavirus Cases in Los Angeles")
plt.xlabel("time (days)")
plt.ylabel("# people")
plt.bar(x5, la_new_cases, color=(0.21, 0.7, 0.23, 1));

plt.subplot(6, 2, 10);
plt.title("Total Coronavirus Cases in Los Angeles")
plt.xlabel("time (days)")
plt.ylabel("# people")
plt.plot(y5, 'g-.', label="Los Angeles")

plt.subplot(6, 2, 11);
plt.title("Daily New Coronavirus Cases in New York City")
plt.xlabel("time (days)")
plt.ylabel("# people")
plt.bar(x6, ny_new_cases);

plt.subplot(6, 2, 12);
plt.title("Total Coronavirus Cases in New York City")
plt.xlabel("time (days)")
plt.ylabel("# people")
plt.plot(y6, 'p-.', label="New York")

plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.3, hspace=1.5)

plt.show()
