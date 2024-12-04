filename = "input.txt"
list_digits = [str(k) for k in range(10)]

symbols_matrix = []
adjacency_values = {}
with open(filename) as file:
    for i,line in enumerate(file.readlines()):
        line_list = []
        for j, element in enumerate(line):
            if element == "*":
                line_list.append(1)
                adjacency_values[(i,j)] = []
            else:
                line_list.append(0)
        symbols_matrix.append(line_list)

with open(filename) as file:
    identified_digits = []
    for i,line in enumerate(file.readlines()):
        _j = 0
        for j,element in enumerate(line):
            if j<_j:
                continue
            if element in list_digits:
                digit = element
                _j = j+1
                while line[_j] in list_digits\
                    and _j <= len(line)-1:
                        digit = f"{digit}{line[_j]}"
                        _j+=1
                
                try:
                    if 1 == symbols_matrix[i][_j]:
                        adjacency_values[(i,_j)].append(digit)
                        continue
                except:
                    pass
                
                try:
                    if 1 == symbols_matrix[i][j-1]:
                        adjacency_values[(i,j-1)].append(digit)
                        continue
                except:
                    pass
                
                try:
                    if 1 == symbols_matrix[i-1][_j]:
                        adjacency_values[(i-1,_j)].append(digit)
                        continue
                except:
                    pass
                
                try:
                    if 1 == symbols_matrix[i+1][_j]:
                        adjacency_values[(i+1,_j)].append(digit)
                        continue
                except:
                    pass
                
                try:
                    for k in range(j,_j+1):
                        if 1 == symbols_matrix[i-1][k]:
                            adjacency_values[(i-1,k)].append(digit)
                            continue
                except:
                    pass
                
                try:
                    for k in range(j,_j+1):
                        if 1 == symbols_matrix[i+1][k]:
                            adjacency_values[(i+1,k)].append(digit)
                            continue
                except:
                    pass
                
                try:
                    if 1 == symbols_matrix[i+1][j-1]:
                        adjacency_values[(i+1,j-1)].append(digit)
                        continue
                except:
                    pass
                
                try:
                    if 1 == symbols_matrix[i-1][j-1]:
                        adjacency_values[(i+1,j-1)].append(digit)
                        continue
                except:
                    pass

print(adjacency_values)
res = 0
for key, val in adjacency_values.items():
    if len(val) == 2:
        ratio = int(val[0])*int(val[1])
        res += ratio

print(res)
                
                        
            