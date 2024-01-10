import matplotlib.pyplot as plt
import csv
name = input("input your name of the csv file: ")
name2 = input("input the title of your graph: ")
f = open(name)
data = csv.reader(f)
x = []
y = []
for row in data:
    if float(row[1]) > 0.0:
        x.append(float(row[0]))
        y.append(float(row[1]))
plt.title(name2)
plt.plot(x, y)
plt.show()
f.close()
