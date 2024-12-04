from collections import deque
FILENAME = "input.txt"
# Get the maze :
MAZE = open(FILENAME).read().splitlines()
assert len(MAZE) == len(MAZE[0])
size = len(MAZE)
steps = 26501365
assert steps % size == size //2

# The start point of the maze is the exact center of the maze :
start_i, start_j = len(MAZE)//2,len(MAZE[0])//2
# Possible directions to test when make steps :
directions = [(0,1),(0,-1),(1,0),(-1,0)]

def fill(start_i, start_j, nsteps):
    # Records of final possible positions, seen points :
    final_positions = set()
    seen = set()
    # queue to evaluate positions (i,j,steps_remaining):
    queue = deque([(start_i,start_j,nsteps)])

    # While there are possibilites to test in the queue :
    while queue:
        # we take+pop the last element of the queue:
        i,j,N = queue.popleft()
        
        # if number of steps remaining is even, it is possible to go back to this point
        # so we add it to possible final positions
        if N % 2 == 0:
            final_positions.add((i,j))
        # if number of steps remaining is 0 we continue as we dont have remaining steps:
        if N == 0:
            continue
        
        # we loop across all possible positions :
        for direction in directions:
            di,dj = direction
            ni, nj = i+di, j+dj
            # if new position is in the grid :
            if 0<=ni<len(MAZE) and 0<=nj<len(MAZE[0]):
                # if new position doesnt end up in a bush and has not been seen :
                if MAZE[ni][nj]!="#" and (ni,nj) not in seen:
                    
                    # we add it to seen and to the queue to test it :
                    seen.add((ni,nj))
                    queue.append((ni,nj,N-1))

    # print the total number of possible final positions :
    return len(final_positions)

grid_width = steps = steps // size - 1
odd = (grid_width //2 * 2 + 1) ** 2
even = ((grid_width + 1) // 2 * 2) ** 2 

even_points = fill(start_i, start_j, size*2)
odd_points = fill(start_i, start_j, size * 2 + 1)

corner_t = fill(size - 1, start_j, size - 1)
corner_r = fill(start_i, 0, size - 1)
corner_b = fill(0, start_j, size - 1)
corner_l = fill(start_i, size - 1, size - 1)

small_tr = fill(size - 1, 0, size // 2 - 1)
small_tl = fill(size - 1, size - 1, size // 2 - 1)
small_br = fill(0, 0, size // 2 - 1)
small_bl = fill(0, size - 1, size // 2 - 1)

large_tr = fill(size - 1, 0, size * 3 // 2 - 1)
large_tl = fill(size - 1, size - 1, size * 3 // 2 - 1)
large_br = fill(0, 0, size * 3 // 2 - 1)
large_bl = fill(0, size - 1, size * 3 // 2 - 1)


print(
    odd * odd_points +
    even * even_points +
    corner_t + corner_r + corner_b + corner_l +
    (grid_width + 1) * (small_tr + small_tl + small_br + small_bl) +
    grid_width * (large_tr + large_tl + large_br + large_bl)
)