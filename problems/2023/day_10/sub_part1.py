filename = "input.txt"
pipes = [p for p in "F-7|LJ"]
# ,"S":[(0,-1),(0,1),(-1,0),(1,0)]
valid_pipes = {
    "S":{"F":[],"-":[],"7":[],"|":[],"L":[],"J":[]},
    "F":{"|":[(1,0)],"L":[(1,0)],"J":[(1,0),(0,1)],"-":[(0,1)],"7":[(0,1)]},
    "-":{"F":[(0,-1)],"-":[(0,-1),(0,1)],"L":[(0,-1)],"7":[(0,1)],"J":[(0,1)]},
    "7":{"-":[(0,-1)],"|":[(1,0)],"L":[(0,-1),(1,0)],"F":[(0,-1)],"J":[(1,0)]},
    "|":{"F":[(-1,0)],"7":[(-1,0)],"L":[(1,0)],"J":[(1,0)],"|":[(-1,0),(1,0)]},
    "L":{"|":[(-1,0)],"-":[(0,1)],"J":[(0,1)],"7":[(0,1),(-1,0)],"F":[(-1,0)]},
    "J":{"|":[(-1,0)],"-":[(0,-1)],"F":[(-1,0),(0,-1)],"7":[(-1,0)],"L":[(0,-1)]}
    }

def adjacent_pipes(matrix, i, j):
    possible_adjacents = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    adjacents = []
    for (i_,j_) in possible_adjacents:
        if i_>=0 and i_<=len(matrix)-1:
            if j_>=0 and j_<=len(matrix[0])-1:
                if matrix[i_][j_] in pipes:
                    adjacents.append((i_,j_))
    return adjacents
 
def valid_adjacent_pipes(matrix, adjacent_pipes, i,j):
    res = []
    pipe = matrix[i][j]
    if pipe == "S":
        return adjacent_pipes
    for i_,j_ in adjacent_pipes:
        relative_i = i_-i
        relative_j = j_-j
        relative_coords = (relative_i,relative_j)
        for valid_pipe, valid_positions in valid_pipes[pipe].items():
            if matrix[i_][j_]==valid_pipe and relative_coords in valid_positions:
                res.append((i_,j_))
    return res
                
with open(filename) as file:
    land_matrix = []
    for line in file.readlines():
        land_matrix.append(line)

with open(filename) as file:
    paths_len = []
    for i,line in enumerate(file.readlines()):
        for j,element in enumerate(line):
            if element == "S":
                print("S in position ", i,j)
                list_adjacent_pipes = adjacent_pipes(land_matrix,i,j)
                for (i,j) in list_adjacent_pipes:
                    steps=0
                    position_i = i
                    position_j = j
                    reach_S = False
                    positions_history = []
                    while True:
                        list_adjacent_pipes = adjacent_pipes(land_matrix,position_i,position_j)
                        list_adjacent_pipes = [(i,j) for (i,j) in list_adjacent_pipes if (i,j) not in positions_history]
                        print("adjacent pipes :", list_adjacent_pipes)
                        v = valid_adjacent_pipes(land_matrix, list_adjacent_pipes, position_i,position_j)
                        print("valide pipe :", v)
                        if len(v) == 0:
                            break
                        positions_history.append((position_i, position_j))
                        position_i, position_j = v[0]
                        steps +=1
                        print(land_matrix[position_i][position_j])
                    paths_len.append(int((steps+1)/2))

print("****")
print(max(paths_len)+1)