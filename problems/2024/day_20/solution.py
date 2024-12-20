import argparse
import re
from collections import deque
from tqdm import tqdm

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall('[-+]?\d+', string)))
  
  @staticmethod
  def manhattan_distance(r1, c1, r2, c2):
    return sum(abs(v1-v2) for v1,v2 in zip((r1,c1),(r2,c2)))
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.grid = [list(line) for line in self.file.splitlines()]
    self.nrows, self.ncols = len(self.grid), len(self.grid[0])
    
    # get start and end coordinates
    for r in range(self.nrows):
      for c in range(self.ncols):
        if self.grid[r][c] == 'S':
          self.start = (r, c)
        elif self.grid[r][c] == 'E':
          self.end = (r, c)
  
  @staticmethod
  def solve_maze(grid: list[list[str]], start: tuple[int], end: tuple[int]):
    """simple solving maze function based on DFS algorithm

    Args:
        grid (list[list[str]]): 2D grid representing the maze ("#"=walls,"."=possible paths)
        start (tuple[int]): starting coordinates
        end (tuple[int]): ending coordinates

    Returns:
        t, seen: time taken to reach the end of the maze, and seen positions during the search
    """
    sr, sc = start
    er, ec = end
    Q = deque([(sr, sc, 0)])
    seen = []
    while Q:
      r, c, t = Q.popleft()
      if (r,c) == (er, ec):
        seen.append((r,c))
        return t, seen
      if (r,c) in seen:
        continue
      seen.append((r,c))
      for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
        nr, nc = r+dr, c+dc
        if grid[nr][nc] != '#':
          Q.append((nr, nc, t+1))
  
  def get_num_bests_cheats(self, max_cheat_time: int, cheat_save_time_threshold: int):
    """function to obtain number of possible cheat trajectories that allows to save at least N=cheat_save_time_threshold 
    compared to a regular run without any cheat

    Args:
        max_cheat_time (int): maximum cheating time
        cheat_save_time_threshold (int): threshold to consider the cheat trajectory as a good one (compared to regular run)

    Returns:
        int: number of good trajectories using legit cheat
    """
    # cache for efficiency
    cache_time = {}
    # solve maze as a regular run to obtain legit path and legit time
    T, history = self.solve_maze(grid=self.grid, start=self.start, end=self.end)
    # list to add all 
    n_good_cheats = 0
    # range across all possible moments to cheat one time
    for t, (r,c) in tqdm(enumerate(history)):
      # t1 = time elasped before cheat moment
      t1 = len(history[:t+1])
      # compute all reacheable coordinates based on max cheat time (manhattan distance and not a wall at the end):
      possible_coords = [(r2,c2) for r2 in range(self.nrows) for c2 in range(self.ncols) 
                         if self.manhattan_distance(r, c, r2, c2) <= max_cheat_time 
                         and (r,c) != (r2,c2) 
                         and self.grid[r2][c2] != '#']
      # loop across all legit ending cheat positions
      for nr, nc in possible_coords:
        # t2= cheat time (-2 to dont count first and last multiple times in the count)
        t2 = self.manhattan_distance(r, c, nr, nc)-2
        # t3 = time elapsed from just after the cheat to the end
        if (nr,nc) in cache_time:
          t3 = cache_time[(nr,nc)]
        else:
          idx = [i for i,coord in enumerate(history) if coord == (nr,nc)][0]
          t3 = len(history[idx:])
          cache_time[(nr,nc)] = t3
        # if the cheating sequence allows to win sufficient time, add one to the count
        if T-(t1+t2+t3) >= cheat_save_time_threshold:
          n_good_cheats +=1
    
    return n_good_cheats
    
  def part1(self):
    return self.get_num_bests_cheats(max_cheat_time=2, cheat_save_time_threshold=100)
  
  def part2(self):
    return self.get_num_bests_cheats(max_cheat_time=20, cheat_save_time_threshold=100)
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
