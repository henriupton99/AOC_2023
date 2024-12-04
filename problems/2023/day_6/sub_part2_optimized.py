# NAIVE VERSION : try all waiting times, very 
import re
import time
from math import sqrt, floor

start = time.time()
with open("input.txt") as file:
    for line in file:
        if line.__contains__("Time"):
            race_time = int("".join(re.findall("[0-9]+",line)))
        if line.__contains__("Distance"):
            distance = int("".join(re.findall("[0-9]+",line)))

# If t = waiting time and  T = race time, then speed is t and distance travelled is d(t,T)=t*(T-t)
# Then by considering d_ the record distance to beat and solving the inequation d(t,T)>d we have:
# d(t,T)>d <=> t \in [floor((T - sqrt(T**2 -4d_))/2) , floor((T + sqrt(T**2 -4d_))/2)]

T = race_time
d_ = distance
print(len(range(floor((T - sqrt(T**2 - 4*d_))/2),floor((T + sqrt(T**2 - 4*d_))/2))))
end = time.time()
print("time : ", end-start)