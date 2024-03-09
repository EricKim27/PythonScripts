import matplotlib.pyplot as plt
import csv
import system
name = system.argv[1]
#name_1= input("one more")
#name2 = input("input the title of your graph: ")
name2 = system.argv[2]
f = open(name)
#f1 = open(name_1)
data = csv.reader(f)
#data2 = csv.reader(f1)
x = []
#x1 = []
y = []
#y1 = []
for row in data:
    if float(row[1]) > 0.0:
        x.append(float(row[0]))
        y.append(float(row[1]))
#for row in data2:
#    if float(row[1]) > 0.0:
#        x1.append(float(row[0]))
#        y1.append(float(row[1]))
plt.title(name2)
plt.plot(x, y)
#plt.plot(x1, y1, label='Baseball')
#plt.legend()
plt.show()
f.close()
