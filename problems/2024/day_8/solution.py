import argparse
from collections import defaultdict
from itertools import product

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'

  @staticmethod
  def get_antennas_map(matrix: list[list[str]]):
    nrows, ncols = len(matrix), len(matrix[0])
    antenna_types = defaultdict(list)
    for i in range(nrows):
      for j in range(ncols):
        if matrix[i][j] != '.':
          antenna_types[matrix[i][j]].append(tuple((i,j)))
    return antenna_types
  
  @staticmethod
  def display_matrix(matrix: list[list[str]]) -> None:
    nrows = len(matrix)
    for i in range(nrows):
      print(''.join(matrix[i]))
  
  @staticmethod
  def propagate_antinodes(matrix: list[list[str]], antennas: defaultdict, propagate: bool) -> set[tuple]:
    nrows, ncols = len(matrix), len(matrix[0])
    antinodes = []
    for coords in antennas.values():
      for coords_first, coords_second in list(product(coords, coords)):
        if coords_first == coords_second:
          continue
        di, dj = list(map(lambda i,j: i-j, coords_first, coords_second))
        antinode_i, antinode_j = coords_first[0], coords_first[1]
        if propagate:
          antinodes.append(tuple((antinode_i,antinode_j)))
          out_of_bounds = False
          while not out_of_bounds:
            antinode_i, antinode_j = antinode_i + di, antinode_j + dj
            if 0>antinode_i or antinode_i>nrows-1 or 0>antinode_j or antinode_j>ncols-1:
              out_of_bounds = True
              break
            antinodes.append(tuple((antinode_i,antinode_j)))
            if matrix[antinode_i][antinode_j] == '.':
              matrix[antinode_i][antinode_j] = '#'
        else:
          antinode_i, antinode_j = antinode_i + di, antinode_j + dj
          if 0<=antinode_i<=nrows-1 and 0<=antinode_j<=ncols-1:
            antinodes.append(tuple((antinode_i,antinode_j)))
            if matrix[antinode_i][antinode_j] == '.':
              matrix[antinode_i][antinode_j] = '#'
    return set(antinodes)
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.matrix = [list(line) for line in self.file.splitlines()]
    self.nrows, self.ncols = len(self.matrix), len(self.matrix[0])
    self.antennas = self.get_antennas_map(self.matrix)
    
  def part1(self):
    antinodes = self.propagate_antinodes(self.matrix, self.antennas, propagate=False)
    #self.display_matrix(self.matrix)
    return len(antinodes)
  
  def part2(self):
    antinodes = self.propagate_antinodes(self.matrix, self.antennas, propagate=True)
    #self.display_matrix(self.matrix)
    return len(antinodes)
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
