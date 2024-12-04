import re
with open("input.txt") as file:
    for line in file:
        if line.__contains__("Time"):
            times = [int(t) for t in re.findall("[0-9]+",line)]
        if line.__contains__("Distance"):
            distances = [int(d) for d in re.findall("[0-9]+",line)]
    assert len(times)==len(distances),"Not correct pairs between times and distances"

possibles_ways_to_win = {}
for i, (time, distance) in enumerate(zip(times,distances)):
    win_strategies = []
    for waiting_time in range(1,time):
        remaining_time = time - waiting_time
        speed = waiting_time
        run_distance = remaining_time*speed
        if run_distance > distance:
            win_strategies.append(waiting_time)
    possibles_ways_to_win[i] = win_strategies

product_of_races_win_strategies = 1
for race, win_strategies in possibles_ways_to_win.items():
    product_of_races_win_strategies *= len(win_strategies)
    
print(product_of_races_win_strategies)