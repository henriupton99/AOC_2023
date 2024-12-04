filename = "input.txt"
list_digits = [str(k) for k in range(10)]

symbols_matrix = []
with open(filename) as file:
    for line in file.readlines():
        symbols_matrix.append(
            [1 if element not in list_digits
             and element not in [".","\n"] else 0
             for element in line]
        )

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
                        identified_digits.append(digit)
                        continue
                except:
                    pass
                
                try:
                    if 1 == symbols_matrix[i][j-1]:
                        identified_digits.append(digit)
                        continue
                except:
                    pass
                
                try:
                    if 1 == symbols_matrix[i-1][_j]:
                        identified_digits.append(digit)
                        continue
                except:
                    pass
                
                try:
                    if 1 == symbols_matrix[i+1][_j]:
                        identified_digits.append(digit)
                        continue
                except:
                    pass
                
                try:
                    if 1 in symbols_matrix[i-1][j:_j]:
                        identified_digits.append(digit)
                        continue
                except:
                    pass
                
                try:
                    if 1 in symbols_matrix[i+1][j:_j]:
                        identified_digits.append(digit)
                        continue
                except:
                    pass
                
                try:
                    if 1 == symbols_matrix[i+1][j-1]:
                        identified_digits.append(digit)
                        continue
                except:
                    pass
                
                try:
                    if 1 == symbols_matrix[i-1][j-1]:
                        identified_digits.append(digit)
                        continue
                except:
                    pass

                
print(sum([int(e) for e in identified_digits]))
                
                        
            