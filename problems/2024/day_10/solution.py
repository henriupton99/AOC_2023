import argparse
from collections import defaultdict

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'

  def explore_paths(self, i, j, si, sj):
    """function to explore paths in any direction (up,down,lft,right) given a position (i,j) in the grid,
    by also storing the starting point of the path (si,sj)

    Args:
        i (int): current row index
        j (int): current column index
        si (int): starting row index
        sj (int): starting column index
    """
    #if we reach a tailhead, append current position in the starting position set/list
    if self.grid[i][j] == 9:
      try:
        self.trailheads[(si,sj)].add((i,j))
      except:
        self.trailheads[(si,sj)].append((i,j))
    # try any direction (up, down, left, right)
    for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
      ni, nj = i+di, j+dj
      # if in the grid and we increase of 1, then the neighbor is a valid next position
      if 0<=ni<=self.nrows-1 and 0<=nj<=self.ncols-1 and self.grid[ni][nj] == self.grid[i][j]+1:
        # explore for this valid position
        self.explore_paths(ni, nj, si, sj)
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.grid = [list(map(int, line)) for line in self.file.splitlines()]
    self.nrows, self.ncols = len(self.grid), len(self.grid[0])
 
  def part1(self):
    # first case for part 1: we want to get all reacheable tailheads
    # consider set to remove paths that comes from the same starting point and lead to the same tailhead
    self.trailheads = defaultdict(set) 
    for i in range(self.nrows):
      for j in range(self.ncols):
        if self.grid[i][j] == 0:
          self.explore_paths(i, j, i, j)
    return sum(len(values) for values in self.trailheads.values())
  
  def part2(self):
    # second case for part 2: we want to get all possible paths that lead to tailheads
    # consider list to keep paths that comes from the same starting point and lead to the same tailhead
    self.trailheads = defaultdict(list) 
    for i in range(self.nrows):
      for j in range(self.ncols):
        if self.grid[i][j] == 0:
          self.explore_paths(i, j, i, j)
    return sum(len(values) for values in self.trailheads.values())
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
