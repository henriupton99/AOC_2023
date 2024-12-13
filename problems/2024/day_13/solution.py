import argparse
import re
import numpy as np

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall('\d+', string)))
  
  @staticmethod
  def solve_linear_system(a: list[int], b: list[int], c: list[int]):
    assert len(a) == len(b) == len(c), 'a, b, c must be of samle length'
    return list(map(lambda x: round(x), np.linalg.solve(np.array([a, b]).T, np.array(c))))
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.blocks = list(map(lambda x : x.split('\n'), self.file.split('\n\n')))
    self.shift = 10000000000000
    
  def part1(self):
    result = 0
    for block in self.blocks:
      a, b, p = self.get_nums(block[0]), self.get_nums(block[1]), self.get_nums(block[2])
      s, t = self.solve_linear_system(a, b, p)
      if a[0]*s + b[0]*t == p[0] and a[1]*s + b[1]*t == p[1]:
        result += 3*s + t
    return result
  
  def part2(self):
    result = 0
    for block in self.blocks:
      a, b, p = self.get_nums(block[0]), self.get_nums(block[1]), self.get_nums(block[2])
      p[0], p[1] = p[0] + self.shift, p[1] + self.shift
      s, t = self.solve_linear_system(a, b, p)
      if a[0]*s + b[0]*t == p[0] and a[1]*s + b[1]*t == p[1]:
        result += 3*s + t
    return result
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
