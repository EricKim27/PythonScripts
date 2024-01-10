import time
import csv
initial_speed = 0.0
gravitational_acceleration = 9.8
duration = 0.0
distance = float(input("Please input the height: "))
initial_distance = distance
data = []
while distance > 0:
    initial_speed += gravitational_acceleration * 0.001
    distance -= initial_speed * 0.001
    duration += 0.001
    time.sleep(0.001)
    data.append([duration, distance])

print("The time it took to land is {0} seconds".format(duration))
csv_filename = f"falling_data_{initial_distance}m.csv"
with open(csv_filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)
print("data saved to csv file: {0}".format(csv_filename))
