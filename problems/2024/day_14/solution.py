import argparse
import re

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall('[-+]?\d+', string)))
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.lines = self.file.splitlines()
    
    self.n_seconds = 100
    self.nrows, self.ncols = 103, 101
    
  def part1(self):
    quadrants = [0, 0, 0, 0]
    for line in self.lines:
      px, py, vx, vy = self.get_nums(line) 
      fx = (px + self.n_seconds*vx) % self.ncols
      fy = (py + self.n_seconds*vy) % self.nrows
      if fx < 50 and fy < 51:
        quadrants[0] += 1
      elif fx > 50 and fy < 51:
        quadrants[1] += 1
      elif fx < 50 and fy > 51:
        quadrants[2] += 1
      elif fx > 50 and fy > 51:
        quadrants[3] += 1
    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
  
  def part2(self):
    n_seconds = 1
    n_robots = len(self.lines)
    while True:
      seen  = set()
      for line in self.lines:
        px, py, vx, vy = self.get_nums(line) 
        fx = (px + n_seconds*vx) % self.ncols
        fy = (py + n_seconds*vy) % self.nrows
        seen.add(tuple((fx,fy)))
      if len(seen) == n_robots:
        break
      n_seconds += 1
    return n_seconds
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
