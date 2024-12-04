from collections import defaultdict
import numpy as np
filename = "input.txt"
VISITED = defaultdict(dict[tuple])
DIRMAP = {"U":(-1,0),"D":(1,0),"L":(0,-1),"R":(0,1)}

# Start position :
i,j = 0,0
# boundary points :
b = 0
min_i, max_i, min_j, max_j = 0,0,0,0
for instructions in open(filename).read().splitlines():
    direction, num_steps, color = instructions.split()
    # conversions :
    di,dj = DIRMAP[direction]
    color = color.replace("(","").replace(")","")
    num_steps = int(num_steps)
    for step in range(num_steps):
        i,j = i+di, j+dj
        b += 1
        min_i = min(i,min_i)
        min_j = min(j,min_j)
        max_i = max(i,max_i)
        max_j = max(j,max_j)
        color.replace("(","").replace(")","")
        VISITED[(i,j)] = color

# Get array of edges :
edges = list(VISITED.keys())
# Use shoelace formula to compute A:
# A = sum_{i=1}^{N} (x_i - x_{i+1}) (y_i + y_{i+1})
# 
A = abs(sum((edges[i][0]-edges[(i+1)%len(edges)][0])*(edges[i][1]+edges[(i+1)%len(edges)][1]) for i in range(len(edges))))/2

# Reverse the Pick's formula in order to obtain i=interor points :
# - if A is the area of a polygon
# - if b is the number of its boundary points
# Then : A = i + b/2 -1
i = A - b//2  +1
print(int(i + b))

# VIZUALIZE THE RESULT IN A TXT FILE:
# Number of rows (resp columns) are the distances between minimum and maximum i (resp j) 
# add 1 if minimum and maximum dont have the same sign
NCOLS = abs(max_j)+abs(min_j)+1 #int(min_j<0<max_j)
NROWS = abs(max_i)+abs(min_i)+1 #int(min_i<0<min_j)
BOARD = np.array([["."]*NCOLS for _ in range(NROWS)])
for (i,j),c in VISITED.items():
    i,j = i+abs(min_i),j+abs(min_j)
    BOARD[i,j] = "#"

# If located in (i,j) we see "#" simultaneously on right, left, up, right
# We can dig in (i,j)
for i in range(1,NROWS-1):
    for j in range(1,NCOLS-1):
        if "#" in BOARD[:i+1,j] and "#" in BOARD[i:,j]:
            if "#" in BOARD[i,:j+1] and "#" in BOARD[i,j:]:
                BOARD[i][j] = "#"

# Write the result in a document :
with open("res.txt","w") as file:
    for row in BOARD:
        file.write("".join(row))
        file.write("\n")
