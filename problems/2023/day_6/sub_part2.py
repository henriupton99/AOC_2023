# NAIVE VERSION : try all waiting times, very 
import re
import matplotlib.pyplot as plt
with open("test.txt") as file:
    for line in file:
        if line.__contains__("Time"):
            time = int("".join(re.findall("[0-9]+",line)))
        if line.__contains__("Distance"):
            distance = int("".join(re.findall("[0-9]+",line)))

win_strategies = []
runs_distances = []
for waiting_time in range(time):
    remaining_time = time - waiting_time
    speed = waiting_time
    run_distance = remaining_time*speed
    runs_distances.append(run_distance)
    if run_distance > distance:
        win_strategies.append(waiting_time)

print(len(win_strategies))
plt.plot(range(time),runs_distances)
plt.xlabel("waiting time")
plt.ylabel("distance travelled")
plt.show()