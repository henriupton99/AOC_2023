import heapq
def minimal_heat(start, goal, min_moves, max_moves):
    """Optimal path w.r.t a heat loss, start coordinates and goal coordinates

    Args:
        start (tuple): (i,j) coordinates for start position in 
        end (tuple): _description_
        min_moves (_type_): minimal number of moves in the same direction
        max_moves (_type_): maximal number of moves in the same direction

    Returns:
        heat: cumulated heat score of the optimal path
    """
    i,j = start
    # state = (heat,i,j,di,dj)
    state = [(0,i,j,0,0)]
    visited = set()
    # Infinite loop in order to explore the maze:
    while True:
        # Get minimal heat branch given all explored branches :
        heat,i,j,di,dj = heapq.heappop(state)
        # Terminal condition : the actual state is the goal state
        if (i,j) == goal:
            return heat
        # Condition to avoid from looping (optimal step never do the same exact moves) :
        if (i,j,di,dj) in visited:
            continue
        # Add current state to visited states :
        visited.add((i,j,di,dj))
        # Compute different branches (indeed optimal path dont simply take the minimal neighbor heat)
        for di,dj in {(1,0),(0,1),(-1,0),(0,-1)}-{(di,dj),(-di,-dj)}:
            a,b,h = i,j,heat
            # Repeat the moves in the same direction given the boundaries (min_moves, max_moves)
            for n_moves in range(1,max_moves+1):
                a,b = a+di,b+dj
                # Check if coordinates (a,b) dont exceed the limit of the maze:
                if (a,b) in maze:
                    h += maze[a,b]
                    if n_moves>=min_moves:
                        # Push the valid state to the list of branches to evaluate in the "heappop" pass 
                        heapq.heappush(state, (h, a,b, di,dj))

filename = "input.txt"
maze = {(i,j): int(c) for i,r in enumerate(open(filename)) for j,c in enumerate(r.strip())}
print(minimal_heat((0,0),max(maze), 1, 3))