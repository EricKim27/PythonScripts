import time
import csv
import math

initial_speed = 0.0
gravitational_acceleration = 9.8
duration = 0.0
distance = float(input("Please input the height: "))
mass = float(input("input the mass of your object: "))
refarea = 0.01
airdensity=1.2
initial_distance = distance
data = []
while distance > 0:
    terminal_velocity = math.sqrt((2 * mass * gravitational_acceleration) / (airdensity * refarea))
    drag_coefficient = 2 * mass * gravitational_acceleration / (airdensity * refarea * terminal_velocity**2)
    air_resistance = -drag_coefficient * initial_speed
    initial_speed += (gravitational_acceleration + air_resistance) * 0.001
    distance -= initial_speed * 0.001
    duration += 0.001
    time.sleep(0.001)
    data.append([duration, distance])

print("The time it took to land is {0} seconds".format(duration))
csv_filename = f"./Result/falling_data_{initial_distance}m.csv"
with open(csv_filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)
print("data saved to csv file: {0}".format(csv_filename))
