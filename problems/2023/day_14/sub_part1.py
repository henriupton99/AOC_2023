maze = [list(line) for line in open("input.txt").read().split("\n")]
replacements = 1

while replacements > 0:
    replacements = 0
    for j in range(len(maze[0])):
        for i in range(1,len(maze)):
            if maze[i-1][j] == "." and maze[i][j] == "O":
                maze[i-1][j] = "O"
                maze[i][j] = "."
                replacements += 1

ans = 0
for i,row in enumerate(maze):
    num_rocks = sum([element == "O" for element in row])
    ans += num_rocks * (len(maze)-i)

print(ans)