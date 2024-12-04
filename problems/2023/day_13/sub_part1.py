import numpy as np

def find_reflexion(maze : list, row: bool):
    if row:
        reflexion_row_id = False
        for i in range(1,maze.shape[0]):
            w = min(i,maze.shape[0]-i)
            if np.all(maze[i-w:i,:] == np.flipud(maze[i:i+w,:])):
                reflexion_row_id = i
        return reflexion_row_id
    else :
        reflexion_col_id = False
        for j in range(1,maze.shape[1]):
            w = min(j,maze.shape[1]-j)
            if np.all(maze[:,j-w:j] == np.fliplr(maze[:,j:j+w])):
                reflexion_col_id = j
        return reflexion_col_id

with open("input.txt") as file:
    mazes = []
    maze = []
    for line in file.readlines():
        if line.__contains__("#") or line.__contains__("."):
            maze.append([e for e in line.replace("\n","")])
        else:
            mazes.append(np.array(maze))
            maze = []
    if maze:
        mazes.append(np.array(maze))

ans = 0
for maze in mazes:
    for row in [True,False]:
        coeff = 100 if row else 1
        index = find_reflexion(maze, row)
        if index:
            ans += coeff * index

print(ans) 