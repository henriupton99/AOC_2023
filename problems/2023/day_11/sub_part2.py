import itertools
import numpy as np

with open("input.txt") as file:
    universe = []
    for i,line in enumerate(file.readlines()):
        universe.append([e for e in line.replace("\n","")])
universe = np.array(universe)

expand_rows = [i for i,e in enumerate(np.all(universe==".",axis=1)) if e]
expand_cols = [j for j,e in enumerate(np.all(universe==".",axis=0)) if e]

galaxies_count = 1
galaxies_coords = {}
for i in range(universe.shape[0]):
    for j in range(universe.shape[1]):
        if universe[i,j] == "#":
            galaxies_coords[galaxies_count] = (i,j)
            galaxies_count += 1

distances = {}
for g1,g2 in itertools.combinations([k for k in range(1,galaxies_count)],2):
    extension_row_coeff, extension_col_coeff = 0,0
    i_g1, j_g1 = galaxies_coords[g1]
    i_g2, j_g2 = galaxies_coords[g2]
    for i in expand_rows:
        if min(i_g1,i_g2) < i < max(i_g1,i_g2):
            extension_row_coeff += 1e6-1
    for j in expand_cols:
        if min(j_g1,j_g2) < j < max(j_g1,j_g2):
            extension_col_coeff += 1e6-1
    distances[(g1,g2)] = extension_row_coeff+abs(i_g1-i_g2) + abs(j_g1-j_g2)+extension_col_coeff

res = sum(distances.values())
print(res)