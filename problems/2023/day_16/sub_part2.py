from collections import defaultdict
import sys
import tqdm
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

labyrinth = open("input.txt").read().splitlines()
max_beams = 0
for row in tqdm.tqdm(range(len(labyrinth))):
    for col in range(len(labyrinth[0])):
        start_positions = [(row-1, 0),(row-1,len(labyrinth)),(0,col-1),(col-1,len(labyrinth[0]))]
        start_directions = [(0, 1),(0,-1),(1, 0),(-1,0)]
        for (start_position,start_direction) in zip(start_positions, start_directions):
            visited = defaultdict(list)
            explore(start_position[0], start_position[1], start_direction, labyrinth, visited)
            max_beams = max(max_beams, len(visited.keys()))
          
    print(max_beams)

print(max_beams)
