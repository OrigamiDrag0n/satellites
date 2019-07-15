import csv
from numpy import array
import matplotlib.pyplot as plt
from datetime import datetime

def open_file(filename):
    times = []
    users = []

    with open(f"D:\{filename}.csv",mode = "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            #print(row)
            try:
                users.append(int(row[6][:-2]))
                times.append(datetime(int(row[0][3:]),int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(float(row[5].split("`")[0])), int(float(row[5].split("`")[1][:-1]))))
            except (IndexError, ValueError):
                pass

    return (array(times), array(users))

plt.plot(*open_file("satellite_nyc"), label = "Satellites over New York")
plt.legend()
plt.ylabel("Number of Satellites overhead")
plt.xlabel("GMT -5hrs")
plt.title("Satellites over New York")
plt.gcf().autofmt_xdate()

plt.show()
