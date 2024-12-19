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
    self.stripes, self.designs = self.file.split('\n\n')
    self.stripes = self.stripes.replace(" ","").split(',')
    self.designs = self.designs.split('\n')[:-1]
    self.cache = {}
  
  def solve(self, design: str, stripes: list[str], cache: dict):
    if design not in cache:
      if len(design) == 0:
        return 1
      else:
        result = 0
        for stripe in stripes:
          if design.startswith(stripe):
            result += self.solve(design[len(stripe):], stripes, cache)
        cache[design] = result
    return cache[design]

  def part1(self):
    return sum(self.solve(design, self.stripes, self.cache) > 0 for design in self.designs)
  
  def part2(self):
    return sum(self.solve(design, self.stripes, self.cache) for design in self.designs)
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
