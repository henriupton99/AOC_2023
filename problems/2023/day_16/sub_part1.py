from collections import defaultdict
import sys
sys.setrecursionlimit(5000)
DIRECTIONS_MAPPING = {(0,1):"l",(0,-1):"r",(1,0):"u",(-1,0):"d"}
REFLEXION_MAPPING = {
    ".":{"u":[(1,0)],"d":[(-1,0)],"l":[(0,1)],"r":[(0,-1)]},
    "|":{"u":[(1,0)],"d":[(-1,0)],"l":[(1,0),(-1,0)],"r":[(1,0),(-1,0)]},
    "-":{"u":[(0,1),(0,-1)],"d":[(0,1),(0,-1)],"l":[(0,1)],"r":[(0,-1)]},
    "\\":{"u":[(0,1)],"d":[(0,-1)],"l":[(1,0)],"r":[(-1,0)]},
    "/":{"u":[(0,-1)],"d":[(0,1)],"l":[(-1,0)],"r":[(1,0)]}      
    }

def explore(x, y, direction, labyrinth, visited):
    if x < 0 or y < 0 or x >= len(labyrinth) or y >= len(labyrinth[0]) or direction in visited[(x,y)]:
        return visited
    
    visited[(x,y)].append(direction)
    
    cell = labyrinth[x][y]
    orientation = DIRECTIONS_MAPPING[direction]
    directions = REFLEXION_MAPPING[cell][orientation]
    for direction in directions:
        explore(x+direction[0], y+direction[1], direction, labyrinth, visited)

start_position = (0, 0)
start_direction = (0, 1)  # Starting by moving right
labyrinth = open("input.txt").read().splitlines()
visited = defaultdict(list)
explore(start_position[0], start_position[1], start_direction, labyrinth, visited)

RESULT = [["."] * len(labyrinth[0]) for _ in range(len(labyrinth))]
for i,j in visited.keys():
    RESULT[i][j] = "#"

for line in RESULT:
    print(line)
    
print(len(visited.keys()))
