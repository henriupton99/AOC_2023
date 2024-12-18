import argparse
import re
from typing import Union
from collections import deque

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall('[-+]?\d+', string)))
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.obstructed_coords = self.file.splitlines()
    
    self.grid_size = 6 if test else 70
    self.kb_quota = 12 if test else 1024
  
  def search_exit(self, kb_quota: int) -> Union[None, list[int]]:
    """search exit function that find exits in a grid with obstructed coordinates (amount of n=kb_quota)

    Args:
        kb_quota (int): number of obstructed coordinates (x,y) to consider in the full list of obstructed coordinates

    Returns:
        list of (final x, final y, number of steps) of final point is reacheable, else None
    """
    # generate grid given the given kb quota
    self.coords = [tuple((x,y)) for (x,y) in list(map(self.get_nums, self.obstructed_coords[:kb_quota]))]
    self.grid = [['.' for _ in range(self.grid_size+1)] for _ in range(self.grid_size+1)]
    for (x,y) in self.coords: self.grid[y][x] = '#'
    
    # deque to explore all possible paths with seen history to dont loop
    Q = deque([(0,0,0)])
    seen = set()
    while Q:
      r, c, n = Q.popleft()
      if (r, c) == (self.grid_size, self.grid_size):
        return list([r, c, n])
      # if already seen, dont evaluate it 
      if (r, c) in seen:
        continue
      seen.add((r,c))
      for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
        nr, nc = r+dr, c+dc
        # if deltaed point is in the grid and is not obstructed, add it to the queue
        if 0<=nr<=self.grid_size and 0<=nc<=self.grid_size:
          if self.grid[nr][nc] != "#":
            Q.append((nr, nc, n+1))
    return None
    
  def part1(self):
    # just search for exit with the given amount of kbs
    return self.search_exit(kb_quota=self.kb_quota)
  
  def part2(self):
    # wa can start with the kb quota of part 1 since we know there is an answer for it
    for kb_quota in range(self.kb_quota, len(self.obstructed_coords)):
      if not self.search_exit(kb_quota):
        return self.obstructed_coords[kb_quota-1]
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
