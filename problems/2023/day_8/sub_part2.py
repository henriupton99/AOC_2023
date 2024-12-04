import re
from math import lcm

with open("input.txt") as file:
    maze = {}
    for i,line in enumerate(file.readlines()):
        matches = re.findall("[A-Z]+",line)
        # instructions: 
        if i == 0:
            instructions = [direction for direction in matches[0]]
        if len(matches) == 3:
            maze[matches[0]] = {"L": matches[1], "R":matches[2]}
            
actual_locs = [loc for loc in maze.keys() if loc.endswith("A")]
paths_steps = []
for loc in actual_locs:
    actual_loc = loc
    step_count = 0
    while not loc.endswith("Z"):
        instruction = step_count % len(instructions)
        loc = maze[loc][instructions[instruction]]
        step_count += 1
    paths_steps.append(step_count)

print(lcm(*paths_steps))
