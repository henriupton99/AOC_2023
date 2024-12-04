import re
with open("input.txt") as file:
    maze = {}
    for i,line in enumerate(file.readlines()):
        matches = re.findall("[A-Z]+",line)
        # instructions: 
        if i == 0:
            instructions = [direction for direction in matches[0]]
        if len(matches) == 3:
            maze[matches[0]] = {"L": matches[1], "R":matches[2]}

actual_loc = "AAA"
step_count = 0
while actual_loc != "ZZZ":
    instruction = step_count % len(instructions)
    actual_loc = maze[actual_loc][instructions[instruction]]
    step_count += 1