import matplotlib.pyplot as plt
import tqdm
maze = [list(line) for line in open("input.txt").read().split("\n")]
replacements = 1

def cycle(maze):
    # NORTH 
    replacements = 1
    while replacements > 0:
        replacements = 0
        for j in range(len(maze[0])):
            for i in range(1,len(maze)):
                if maze[i-1][j] == "." and maze[i][j] == "O":
                    maze[i-1][j] = "O"
                    maze[i][j] = "."
                    replacements += 1

    # WEST
    replacements = 1
    while replacements > 0:
        replacements = 0
        for j in range(1,len(maze[0])):
            for i in range(len(maze)):
                if maze[i][j-1] == "." and maze[i][j] == "O":
                    maze[i][j-1] = "O"
                    maze[i][j] = "."
                    replacements += 1

    # SOUTH
    replacements = 1
    while replacements > 0:
        replacements = 0
        for j in range(len(maze[0])):
            for i in range(len(maze)-1):
                if maze[i+1][j] == "." and maze[i][j] == "O":
                    maze[i+1][j] = "O"
                    maze[i][j] = "."
                    replacements += 1
    
    # EAST
    replacements = 1
    while replacements > 0:
        replacements = 0
        for j in range(len(maze[0])-1):
            for i in range(len(maze)):
                if maze[i][j+1] == "." and maze[i][j] == "O":
                    maze[i][j+1] = "O"
                    maze[i][j] = "."
                    replacements += 1
    return maze

NUM_CYCLES = 200
LOADS = []
for k in tqdm.tqdm(range(1,NUM_CYCLES+1)):
    maze = cycle(maze)
    #print(f"After {k} cycle : \n {np.array(maze)}")
    
    ans = 0
    for i,row in enumerate(maze):
        num_rocks = sum([element == "O" for element in row])
        ans += num_rocks * (len(maze)-i)
    
    LOADS.append(ans)

print(LOADS[-50:])
plt.plot(LOADS[-50:])
plt.show()
print(ans)