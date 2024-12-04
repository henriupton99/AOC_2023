from collections import defaultdict
filename = "input.txt"
VISITED = defaultdict(dict[tuple])
DIRMAP = {"3":(-1,0),"1":(1,0),"2":(0,-1),"0":(0,1)}

# Start position :
EDGES = [(0,0)]
# boundary points :
b = 0
for instructions in open(filename).read().splitlines():
    _, _, x = instructions.split()
    x = x[2:-1]
    num_steps = int(x[:-1],16)
    b += num_steps
    di,dj = DIRMAP[x[-1]]
    i, j = EDGES[-1]
    EDGES.append((i+di*num_steps, j+dj*num_steps))
    
# Use shoelace formula to compute A:
# A = sum_{i=1}^{N} (x_i - x_{i+1}) (y_i + y_{i+1})
A = abs(sum((VISITED[i][0]-VISITED[(i+1)%len(VISITED)][0])*(VISITED[i][1]+VISITED[(i+1)%len(VISITED)][1])\
    for i in range(len(VISITED))))/2

# Reverse the Pick's formula in order to obtain i=interor points :
# - if A is the area of a polygon
# - if b is the number of its boundary points
# Then : A = i + b/2 -1
i = A - b//2  +1
print(int(i + b))
