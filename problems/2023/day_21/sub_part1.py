from collections import deque
FILENAME = "input.txt"
# Get the maze :
MAZE = open(FILENAME).read().splitlines()

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

print(fill(start_i, start_j, 64))